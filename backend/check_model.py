from app.ml.shap_explainer import explain_prediction

prediction, shap_data = explain_prediction(
    [250, 12, 3, 25, 8, 10, 5, 0.6, 240]
)

print(prediction)
print(shap_data)