import mlflow
import mlflow.sklearn
import pandas as pd  # Usar pandas para carregar o CSV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlflow.models.signature import infer_signature
from data_processing.preprocessing import clean_data  # Certifique-se de que a função 'clean_data' existe
import sys
import os

# Adicionar caminho para importações de outros diretórios
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Carregar e processar os dados
df = pd.read_csv("data/water_potability.csv")  # Carregando com pandas
df = clean_data(df)  # Certifique-se de que a função 'clean_data' esteja implementada corretamente
X = df.drop(columns=["Potability"])
y = df["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Registrar o modelo no MLflow
with mlflow.start_run() as run:
    signature = infer_signature(X_train, y_train)
    mlflow.sklearn.log_model(model, "random_forest_model", signature=signature)
    
    # Obter o run_id da execução
    run_id = run.info.run_id
    print(f"Run ID: {run_id}")  # Imprime o Run ID da execução atual
    print(f"Acurácia do modelo: {accuracy:.4f}")
