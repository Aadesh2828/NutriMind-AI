from fastapi import APIRouter

from app.schemas.chatbot import ChatRequest, ChatResponse
from app.services.chatbot_service import ask_chatbot


router = APIRouter(
    prefix="/chatbot",
    tags=["AI Nutrition Assistant"]
)


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    answer = ask_chatbot(request.question)

    return ChatResponse(
        answer=answer
    )