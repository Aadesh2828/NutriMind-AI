import joblib
from pathlib import Path
import pandas as pd

# backend/app
BASE_DIR = Path(__file__).resolve().parent.parent

# backend/app/models/randomforestmodel.pkl
MODEL_PATH = BASE_DIR / "models" / "randomforestmodel.pkl"

model = joblib.load(MODEL_PATH)

FEATURES = [
    "energy_kcal",
    "fat",
    "saturated_fat",
    "carbohydrates",
    "sugars",
    "proteins",
    "fiber",
    "salt",
    "sodium"
]

def predict_nutriscore(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return prediction