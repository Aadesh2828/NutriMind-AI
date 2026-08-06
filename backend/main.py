from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.products import router as product_router
from app.routes.prediction import router as prediction_router


app = FastAPI(
    title="NutriMind AI API",
    description="AI-powered nutrition intelligence platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(
    product_router

)

app.include_router(
    prediction_router,
    prefix="/api",
    tags=["Prediction"]
)


@app.get("/")
def home():

    return {
        "message": "Welcome to NutriMind AI API",
        "status": "running"
    }