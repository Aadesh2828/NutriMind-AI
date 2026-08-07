from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest
from app.services.predictor import predict_nutriscore

router = APIRouter()


@router.post("/predict")
def predict(request: PredictionRequest):

    result = predict_nutriscore(request.model_dump())

    result["predicted_grade"] = result["predicted_grade"].upper()

    return result