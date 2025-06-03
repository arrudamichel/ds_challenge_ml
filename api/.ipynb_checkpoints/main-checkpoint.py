from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime, timedelta

app = FastAPI()
model = joblib.load("models/modelo_vendas.pkl")

class PredictRequest(BaseModel):
    store: int
    dept: int
    start_date: str  # formato: "YYYY-MM-DD"

@app.post("/predict")
def predict_sales(req: PredictRequest):
    start = datetime.strptime(req.start_date, "%Y-%m-%d")
    results = []

    for i in range(4):
        date = start + timedelta(weeks=i)
        data = {
            "Store": req.store,
            "Dept": req.dept,
            "Size": 151315,   # tamanho médio estimado
            "Temperature": 60,  # valor médio
            "Fuel_Price": 3.0,
            "CPI": 220,
            "Unemployment": 7.5,
            "MarkDown1": 1000,
            "MarkDown2": 500,
            "MarkDown3": 300,
            "MarkDown4": 200,
            "MarkDown5": 100,
            "IsHoliday": int(date.strftime("%m-%d") in ["02-10", "09-01", "11-28", "12-25"]),
            "Type": 0,
            "Month": date.month,
            "Week": date.isocalendar()[1]
        }
        df_input = pd.DataFrame([data])
        pred = model.predict(df_input)[0]
        results.append({"week": date.strftime("%Y-%m-%d"), "prediction": round(pred, 2)})

    return {"predictions": results}
