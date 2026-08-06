# 🥗 NutriMind AI – AI-Powered Nutrition Intelligence Platform

## 📌 Overview

NutriMind AI is an AI-powered nutrition intelligence platform designed to help users explore food products, predict nutritional quality, visualize food analytics, and receive AI-driven nutrition guidance. The platform combines Machine Learning, Data Analytics, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG) to deliver evidence-based nutrition insights.

The project uses the **Open Food Facts** dataset stored in **PostgreSQL**, a **Random Forest** model for Nutri-Score prediction, interactive **Tableau Public** dashboards for visualization, and is being extended with a RAG-based AI Nutrition Assistant.

---

# 🚀 Features

### ✅ Product Search

* Search food products stored in PostgreSQL.
* View detailed nutritional information.
* FastAPI REST APIs for product retrieval.
* Interactive React-based UI.

### ✅ Nutri-Score Prediction

Predict the nutritional grade (A–E) of food products using nutritional values such as:

* Energy
* Fat
* Saturated Fat
* Carbohydrates
* Sugars
* Proteins
* Fiber
* Salt
* Sodium

Prediction is performed using a trained **Random Forest Machine Learning model**.

### ✅ Nutrition Analytics Dashboard

Interactive Tableau dashboard embedded directly inside the application showing:

* Nutri-Score distribution
* Nutrition trends
* Product category analysis
* Statistical insights
* Interactive charts and filters

### 🚧 AI Nutrition Assistant (In Progress)

Upcoming module implementing Retrieval-Augmented Generation (RAG).

Planned capabilities:

* Nutrition question answering
* Product comparison
* Healthy food recommendations
* Context-aware responses
* Evidence-based guidance using WHO and FSSAI nutrition summaries
* Gemini LLM integration

---

# 🏗 System Architecture

```text
                React Frontend
                      │
                      ▼
                FastAPI Backend
          ┌───────────┴───────────┐
          ▼                       ▼
     PostgreSQL            ML Prediction Model
(Open Food Facts)       (Random Forest Classifier)
          │
          ▼
   Tableau Dashboard
          │
          ▼
      AI Assistant (RAG)
     (Gemini + Knowledge Base)
```

---

# 💻 Tech Stack

## Frontend

* React.js
* Vite
* CSS3
* Axios

## Backend

* FastAPI
* Python

## Database

* PostgreSQL

## Machine Learning

* Scikit-learn
* Random Forest Classifier
* Pickle

## Data Processing

* Pandas
* NumPy

## Visualization

* Tableau Public

## AI (Upcoming)

* Google Gemini
* RAG
* Embeddings

---

# 📂 Project Structure

```text
NutriMindAI/

├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── database/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── styles/
│   ├── package.json
│   └── vite.config.js
│
├── database/
│   └── import_products.py
│
├── dataset/
│
├── README.md
│
└── .gitignore
```

---

# 📊 Dataset

**Dataset:** Open Food Facts

The dataset contains food products with nutritional attributes including:

* Product Code
* Product Name
* Categories
* Nutri-Score
* NOVA Group
* Energy
* Fat
* Saturated Fat
* Carbohydrates
* Sugars
* Proteins
* Fiber
* Salt
* Sodium

These records are imported into PostgreSQL for efficient searching and retrieval.

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/NutriMindAI.git
cd NutriMindAI
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection_string
```

Start the backend:

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

# 📈 Current Modules

| Module                 | Status         |
| ---------------------- | -------------- |
| Home                   | ✅ Completed    |
| Product Search         | ✅ Completed    |
| Product Details        | ✅ Completed    |
| Nutri-Score Prediction | ✅ Completed    |
| Tableau Dashboard      | ✅ Completed    |
| AI Nutrition Assistant | 🚧 In Progress |
| SHAP Explainability    | 🚧 Planned     |

---

# 🔮 Future Enhancements

* AI Nutrition Assistant using RAG
* WHO & FSSAI nutrition knowledge integration
* SHAP explainability for model predictions
* Product comparison
* Personalized nutrition recommendations
* Voice-enabled chatbot
* User authentication
* Saved chat history
* Favorite products
* Advanced analytics dashboard

---

# 👨‍💻 Contributors

* Aadesh Narawade
* Project Team Members

---

# 📄 License

This project is developed for educational and academic purposes.
