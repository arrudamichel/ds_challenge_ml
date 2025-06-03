# Direcionamento de Ações de Marketing

Projeto tem como objetivo a criação de um modelo preditivo para avaliação de clientes e direcionar as estratégias de marketing. Além diso, estão listadas algumas estratégias para possíveis melhorias no modelo, estratégias para a implantação em conjunto com a equipe de marketing e etapas para criação de uma estratégia de marketing em um produto novo, sem dados históricos de venda.

## Dados e informações

A descrição do case pode ser encontrado no arquivo "case_-_cientista_de_dados_[contabilizei].pdf" e os dados estão armazenados no arquivo "dados_case_-_cientista_de_dados_[contabilizei].xlsx"

## Passos para executar o projeto em ambiente Conda

### 1. Instalar Anaconda

### 2. Criar ambiente Conda
```bash
conda env create -f environment.yml
```

### 3. Ativar ambiente Conda
```bash
conda activate teste_tecnico_contabilizei
```

### 4. Executar jupyter-lab para acesso ao Notebook Python.
```
jupyter-lab
```

### Arquivo de Notebook com Treinamento e analises

```
Direcionamento de ações de Marketing.ipynb
```



### API

```
uvicorn api.main:app --reload
```
