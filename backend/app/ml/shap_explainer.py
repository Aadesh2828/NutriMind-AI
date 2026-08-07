import os
import joblib
import shap
import pandas as pd

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "randomforestmodel.pkl"
)

model = joblib.load(MODEL_PATH)

explainer = shap.TreeExplainer(model)

FEATURE_NAMES = [
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


def explain_prediction(input_data):

    df = pd.DataFrame([input_data], columns=FEATURE_NAMES)

    prediction = model.predict(df)[0]

    explanation = explainer(df)

    class_index = list(model.classes_).index(prediction)

    values = explanation.values[0, :, class_index]

    feature_importance = []

    for feature, value in zip(FEATURE_NAMES, values):

        feature_importance.append({

            "feature": feature.replace("_", " ").title(),

            "impact": round(float(value), 4),

            "direction": "positive" if value >= 0 else "negative",

            "abs_impact": abs(round(float(value),4))

        })

    feature_importance.sort(

        key=lambda x: x["abs_impact"],

        reverse=True

    )

    # only top 5

    feature_importance = feature_importance[:5]

    return prediction, feature_importance