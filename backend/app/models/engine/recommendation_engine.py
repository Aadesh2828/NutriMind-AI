import joblib
import pandas as pd
import numpy as np


class FoodRecommender:
    """
    Content-based food recommendation engine.

    Loads a joblib pickle containing:
      - model    : fitted sklearn NearestNeighbors (metric='cosine')
      - scaler   : fitted StandardScaler used on the training features
      - features : list of nutritional feature column names
      - data     : full product DataFrame (must include 'clean_name')

    Lets the user query by PRODUCT NAME (e.g. "coca cola") instead of
    raw nutrition values. Internally: look up that product's own row,
    grab its already-known feature values, scale them the same way the
    training data was scaled, then ask the fitted KNN model for its
    nearest neighbors.
    """

    def __init__(self, pickle_path: str):
        # -----------------------------
        # Load with joblib (matches how it was saved)
        # -----------------------------
        bundle = joblib.load(pickle_path)

        self.model = bundle["model"]        # fitted NearestNeighbors
        self.scaler = bundle["scaler"]      # fitted StandardScaler
        self.features = bundle["features"]  # list of feature column names
        self.df = bundle["data"].reset_index(drop=True)

        # Fast name -> row index lookup
        self.name_to_index = {
            str(name).strip().lower(): idx
            for idx, name in enumerate(self.df["clean_name"])
        }

    # ---------------------------------------------------
    # Helper: find the closest matching product name
    # ---------------------------------------------------
    def _find_index(self, product_name: str) -> int:
        query = product_name.strip().lower()

        # 1. Exact match
        if query in self.name_to_index:
            return self.name_to_index[query]

        # 2. Substring match fallback (e.g. "coca cola" matches
        #    "coca cola classic 500ml")
        matches = [
            idx for name, idx in self.name_to_index.items()
            if query in name
        ]
        if matches:
            return matches[0]

        raise ValueError(
            f"Product '{product_name}' not found in database. "
            f"Try a different spelling or check available product names."
        )

    # ---------------------------------------------------
    # Main recommendation function
    # ---------------------------------------------------
    def recommend(self, product_name: str, top_k: int = 5):
        """
        Recommend top_k products similar to the given product name.

        Parameters
        ----------
        product_name : str
            Product name entered by the user, e.g. "coca cola".
        top_k : int
            Number of recommendations to return.

        Returns
        -------
        list of dict
            Top-k similar products with similarity scores.
        """
        # -----------------------------
        # Step 1: Find this product's own row
        # -----------------------------
        idx = self._find_index(product_name)
        row = self.df.iloc[[idx]]  # keep as DataFrame (double brackets)

        # -----------------------------
        # Step 2: Get its raw feature vector, scale it
        # the exact same way the training data was scaled
        # -----------------------------
        query_features = row[self.features].fillna(0)
        query_scaled = self.scaler.transform(query_features)

        # -----------------------------
        # Step 3: Ask the fitted KNN model for neighbors.
        # We ask for top_k + 1 because the product itself
        # will always be its own nearest neighbor (distance 0).
        # -----------------------------
        distances, indices = self.model.kneighbors(
            query_scaled,
            n_neighbors=top_k + 1
        )

        # -----------------------------
        # Step 4: Build results, skipping the product itself
        # -----------------------------
        recommendations = []
        for distance, i in zip(distances[0], indices[0]):
            if i == idx:
                continue  # skip itself

            r = self.df.iloc[i]
            # cosine metric in sklearn returns distance = 1 - cosine_similarity
            similarity = round((1 - distance) * 100, 2)

            recommendations.append({
                "product_name": r["clean_name"],
                "nutriscore": r.get("nutriscore_grade", None),
                "energy_kcal": float(r.get("energy_kcal", 0)),
                "fat": float(r.get("fat", 0)),
                "saturated_fat": float(r.get("saturated_fat", 0)),
                "carbohydrates": float(r.get("carbohydrates", 0)),
                "sugars": float(r.get("sugars", 0)),
                "proteins": float(r.get("proteins", 0)),
                "fiber": float(r.get("fiber", 0)),
                "sodium": float(r.get("sodium", 0)),
                "similarity": similarity
            })

            if len(recommendations) == top_k:
                break

        return recommendations


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------
if __name__ == "__main__":
    engine = FoodRecommender(
        r"C:/Users/DELL/Downloads/recommendation/recommendation/models/recommendation_model.pkl"
    )

    user_input = "milk chocolate bar"
    results = engine.recommend(user_input, top_k=5)
    
    print(f"Top 5 recommendations similar to '{user_input}':\n")
    for r in results:
        print(f"{r['product_name']}  |  similarity: {r['similarity']}%  |  "
              f"nutriscore: {r['nutriscore']}  |  energy: {r['energy_kcal']} kcal")
