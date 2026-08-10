import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# ============================
# Load Dataset
# ============================

df = pd.read_csv("C:/Users/saish/OneDrive/Desktop/ML Project/recommendation/dataset/open_food_facts_cleaned.csv")

# Remove duplicate products (optional)
df = df.drop_duplicates(subset="clean_name")

# ============================
# Features
# ============================

FEATURES = [
    "energy_kcal",
    "fat",
    "saturated_fat",
    "carbohydrates",
    "sugars",
    "proteins",
    "fiber",
    "sodium"
]

# Fill missing values
df[FEATURES] = df[FEATURES].fillna(0)

# ============================
# Scale Features
# ============================

scaler = StandardScaler()

X = scaler.fit_transform(df[FEATURES])

# ============================
# Train KNN
# ============================

knn = NearestNeighbors(
    n_neighbors=10,
    metric="cosine",
    algorithm="brute"
)

knn.fit(X)

# ============================
# Save Everything
# ============================

joblib.dump(
    {
        "model": knn,
        "scaler": scaler,
        "features": FEATURES,
        "data": df
    },
    "recommendation_model.pkl"
)

print("Recommendation model created successfully.")