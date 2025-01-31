import mlflow

# Conectar ao servidor de rastreamento (pode ser o local ou remoto)
client = mlflow.tracking.MlflowClient()

# Listar todos os modelos registrados
models = client.search_registered_models()

# Exibir os nomes dos modelos registrados
for model in models:
    print(model.name)
