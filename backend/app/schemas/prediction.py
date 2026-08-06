from pydantic import BaseModel

class PredictionRequest(BaseModel):

    energy_kcal: float
    fat: float
    saturated_fat: float
    carbohydrates: float
    sugars: float
    proteins: float
    fiber: float
    salt: float
    sodium: float