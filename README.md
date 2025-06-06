# Challenge sobre análise de vendas

Projeto tem como objetivo a análise de vendas e descontos no período entre 05/02/2010 e 26/10/2012 de 45 lojas. São solicitados 4 principais objetivos:

1. Prever as vendas de cada departamento em cada loja para o ano seguinte.
2. Propor ações recomendadas com base nos insights obtidos, priorizando aquelas que tenham maior impacto no negócio.
3. Modelar os efeitos dos descontos durante as semanas festivas.
4. Criar uma API que permita ao sistema da loja consultar, por meio de um endpoint, a previsão de vendas para as próximas quatro semanas.

## Dados e informações

A descrição do case pode ser encontrado no arquivo "CHALLENGE DS_ML (3).pdf" ou em sua tradução "Desafio_DS_ML_Portugues.pdf" e os dados estão armazenados na pasta "/data", nos arquivos "Features data set.csv", "sales data-set.csv" e "stores data-set.csv".

## Passos para executar o projeto em ambiente Conda

### 1. Instalar Anaconda

### 2. Criar ambiente Conda
```bash
conda env create -f environment.yml
```

### 3. Ativar ambiente Conda
```bash
conda activate mercadolivre_challenge
```

### 4. Executar jupyter-lab para acesso aos Notebooks Python.
```
jupyter-lab
```

### 5. Executar uvcorn para execução da API FastAPI.
```
uvicorn api.main:app --reload
```

### 6. Acessar a API
```
http://127.0.0.1:8000/docs
```

## Instalação e uso do Git LFS
É necessário o uso do Git LFS para armazenamento de arquivos grandes.

# 1. Instalação do git-lfs
```
brew install git-lfs
```

# 2. Execução
```
git lfs install
```

## Estrutura do projeto

```plaintext
ML Challenge/
│
├── api/
│   └── main.py # Arquivo com código da API
│
├── data/
│   ├── dados_unificados.csv                    # Arquivo gerado durante as analises com alguns preprocessamentos
│   ├── Features data set.csv                   # Arquivo disponibilizado com detalhadas sobre as lojas
│   ├── sales data-set.csv                      # Arquivo disponibilizado com dados de vendas das lojas
│   └── stores data-set.csv                     # Arquivo disponibilizado com dados sobre as lojas
│
├── notebooks/                                  # Jupyter Notebooks para exploração e análise
│   ├── 01_eda_preprocessamento.ipynb           # Notebook para merge de dados e preprocessamentos
│   ├── 02_modelagem_previsao.ipynb             # Notebook para treinamento do modelo de previsão de vendas e previsão 2013
│   ├── 03_analise_insights_venda.ipynb         # Notebook para analise e geração de insights para vendas
│   └── 04_modelagem_descontos.ipynb            # Notebook para modelagem do impacto dos descontos em vendas nos feriados
│
├── model/                                      # Modelos treinados e serializados (.pkl) e arquivos de mapas para API
│
├── environment.yml                             # Arquivo para gerar ambiente de desenvolvimento
├── README.md                                   # Este arquivo
└── .gitignore                                  # Arquivos e pastas a serem ignorados pelo Git
```