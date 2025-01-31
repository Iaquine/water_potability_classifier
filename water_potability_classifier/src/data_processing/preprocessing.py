import pandas as pd
import numpy as np
from pydantic import BaseModel, ValidationError

class WaterSample(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

def load_data(filepath: str) -> pd.DataFrame:
    """Carrega o dataset de um arquivo CSV."""
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Realiza limpeza de dados, imputação de valores e normalização."""
    df = df.dropna()  # Remove linhas com valores nulos
    return df

def validate_sample(data: dict):
    """Valida uma amostra de dados usando Pydantic."""
    try:
        sample = WaterSample(**data)
        return sample
    except ValidationError as e:
        print(f"Erro de validação: {e}")
        return None
