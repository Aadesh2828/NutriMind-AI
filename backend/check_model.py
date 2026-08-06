import pickle

with open("app/models/random_forest_model.pkl", "rb") as f:
    obj = pickle.load(f)

print(type(obj))
print(obj.__class__)
print(hasattr(obj, "predict"))

if hasattr(obj, "predict"):
    print("This is a trained model.")
else:
    print("This is NOT a trained model.")