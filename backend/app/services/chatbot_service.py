import os
from pathlib import Path

import chromadb
import google.generativeai as genai

from sentence_transformers import SentenceTransformer

from dotenv import load_dotenv


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# --------------------------------------------------
# Gemini Model
# --------------------------------------------------

model = genai.GenerativeModel("gemini-3.5-flash")

# --------------------------------------------------
# Embedding Model
# --------------------------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# --------------------------------------------------
# ChromaDB
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_DB = BASE_DIR / "ai" / "vector_db"

client = chromadb.PersistentClient(path=str(VECTOR_DB))

collection = client.get_collection(
    "nutrition_knowledge"
)

# --------------------------------------------------
# Nutrition Question Filter
# --------------------------------------------------

def is_nutrition_question(question):

    question = question.lower()

    keywords = [

        "food",
        "nutrition",
        "healthy",
        "unhealthy",
        "diet",
        "meal",
        "eat",
        "eating",
        "drink",
        "beverage",
        "fruit",
        "vegetable",
        "protein",
        "carbohydrate",
        "carbs",
        "fat",
        "saturated fat",
        "trans fat",
        "fiber",
        "fibre",
        "vitamin",
        "mineral",
        "calcium",
        "iron",
        "zinc",
        "magnesium",
        "sodium",
        "salt",
        "sugar",
        "cholesterol",
        "calories",
        "kcal",
        "energy",
        "ingredient",
        "ingredients",
        "nutri-score",
        "nutrition label",
        "label",
        "snack",
        "breakfast",
        "lunch",
        "dinner",
        "obesity",
        "diabetes",
        "blood pressure",
        "heart disease",
        "processed food",
        "organic",
        "fssai",
        "who"

    ]

    return any(keyword in question for keyword in keywords)


def retrieve_context(question, top_k=3):

    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )

    context = "\n\n".join(results["documents"][0])

    return context


def ask_chatbot(question):

    if not is_nutrition_question(question):

        return (
            "I'm NutriMind AI, and I can only assist with nutrition, "
            "food, diet, health, and food safety related questions."
        )

    context = retrieve_context(question)

    prompt = f"""
You are NutriMind AI, an AI-powered Nutrition Assistant.

Your role is to answer ONLY questions related to:

• Nutrition
• Food products
• Ingredients
• Healthy eating
• Diets
• Vitamins & minerals
• Food safety
• Food labels
• Nutri-Score
• Sugar, salt, fats, protein, carbohydrates, fibre
• Processed foods
• WHO nutrition recommendations
• FSSAI guidelines
• General evidence-based nutrition knowledge

--------------------------------------------------

Instructions:

1. First use the retrieved WHO/FSSAI context below to answer the user's question.

2. If the retrieved context partially answers the question, combine it with your general evidence-based nutrition knowledge.

3. If the information is not present in the retrieved context but is a well-established nutrition fact, answer it clearly.

4. Never invent facts or unsupported health claims.

5. If the user asks for medical diagnosis, prescriptions, treatment plans, or emergency medical advice, politely state that you are not a medical professional and recommend consulting a qualified healthcare provider.

6. If the question is NOT related to food, nutrition, health, diet, ingredients, or food safety, politely refuse by replying exactly:

"I'm NutriMind AI, and I can only assist with nutrition, food, diet, health, and food safety related questions."

7. Keep answers concise, accurate, and easy to understand.

8. When WHO or FSSAI information is used, mention the source naturally, for example:
"According to WHO..."
or
"According to FSSAI..."

--------------------------------------------------

Retrieved Context:

{context}

--------------------------------------------------

User Question:

{question}

--------------------------------------------------

Answer:
"""

    response = model.generate_content(prompt)

    return response.text