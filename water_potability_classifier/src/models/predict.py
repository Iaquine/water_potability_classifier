import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow.pyfunc import load_model

# Carregar o modelo do MLflow
model = load_model("runs:/5de2aba2b3cb4f009e5c18f6c5ca723a/random_forest_model")

# Exemplo de entrada
sample = {
    'ph': 7.5,
    'Hardness': 150.0,
    'Solids': 15000,  # Esse valor deve ser convertido para float64
    'Chloramines': 7.0,
    'Sulfate': 250.0,
    'Conductivity': 300.0,
    'Organic_carbon': 25.0,
    'Trihalomethanes': 80.0,
    'Turbidity': 5.0
}

# Converter o sample para um DataFrame do Pandas e garantir que todas as colunas sejam do tipo float64
sample_df = pd.DataFrame([sample])
sample_df = sample_df.astype('float64')

# Fazer a predição
prediction = model.predict(sample_df)

# Exibir o resultado da predição
print(f"Resultado da predição: {'Potável' if prediction[0] == 1 else 'Não potável'}")
