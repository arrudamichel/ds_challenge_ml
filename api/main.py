from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime
import holidays

app = FastAPI()

try:
    model = joblib.load("model/model.pkl")
    store_depts = joblib.load("model/store_depts.pkl")
    stores = joblib.load("model/stores.pkl")

    type_encoded_dict = joblib.load("model/type_encode.pkl")
    dept_encoded_dict = joblib.load("model/dept_encode.pkl")
    store_encoded_dict = joblib.load("model/store_encode.pkl")
    month_encoded_dict = joblib.load("model/month_encode.pkl")
except Exception as e:
    print(e)

# Obter o calendário de feriados dos EUA para 2013
us_holidays = holidays.US(years=2013)

# Função para saber se há feriado na semana (segunda a domingo)
def is_week_holiday(date):
    week_start = date - pd.Timedelta(days=date.weekday())  # segunda
    week_end = week_start + pd.Timedelta(days=6)           # domingo
    return any(week_start <= pd.to_datetime(d) <= week_end for d in us_holidays)

def add_holiday(df):
    df['IsHoliday'] = df['Date'].apply(is_week_holiday).astype(int)
    return df

def add_store_features(df, store_features):
    df["Type"] = store_features["Type"]
    df["Size"] = store_features["Size"]
    return df

def add_month(df):
    df['Month'] = df['Date'].dt.month
    return df

def add_encode(df):
    flat_mapping = {k: v['Month_encoded'] for k, v in month_encoded_dict.items()}
    df['Month_encoded'] = df['Month'].map(flat_mapping)
    df['Month_encoded']

    flat_mapping = {k: v['Type_encoded'] for k, v in type_encoded_dict.items()}
    df['Type_encoded'] = df['Type'].map(flat_mapping)
    df['Type_encoded']

    
    flat_mapping = {int(k): v['Dept_encoded'] for k, v in dept_encoded_dict.items()}
    df['Dept_encoded'] = df['Dept'].map(flat_mapping)
    df['Dept_encoded']

    flat_mapping = {k: v['Store_encoded'] for k, v in store_encoded_dict.items()}
    df['Store_encoded'] = df['Store'].map(flat_mapping)
    df['Store_encoded']

    return df

class PredictRequest(BaseModel):
    store: int

@app.post("/predict")
def predict_sales(req: PredictRequest):
    store_dpto_dict = store_depts[req.store]
    store_features = stores[req.store]

    today = datetime.today().strftime('%Y-%m-%d')
    weeks_4 = pd.DataFrame({'Date': pd.date_range(today, periods=4, freq='W-FRI')})

    rows = []
    for dept in store_dpto_dict:
        for date in weeks_4['Date']:
            rows.append({'Store': req.store, 'Dept': dept, 'Date': date})

    df = pd.DataFrame(rows)

    df = add_holiday(df)
    df = add_month(df)
    df = add_store_features(df, store_features)
    df = add_encode(df)
    
    features = ['Store_encoded', 'Dept_encoded', 'IsHoliday', 'Type_encoded', 'Size', 'Month_encoded']
    print(df.columns)
    print(df[features])


    df["PredictedSales"] = model.predict(df[features])

    response_features = ['Date', 'Dept', 'IsHoliday', 'PredictedSales']
    return df[response_features].to_dict(orient="records")
