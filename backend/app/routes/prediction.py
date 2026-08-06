from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest
from app.services.predictor import predict_nutriscore

router = APIRouter()

@router.post("/predict")
def predict(request: PredictionRequest):
    prediction = predict_nutriscore(request.model_dump())

    return {
        "predicted_grade": prediction.upper()
    }