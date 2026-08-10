import pickle

path = r"C:/Users/saish/OneDrive/Desktop/ML Project/recommendation/models/recommendation_model.pkl"

with open(path, "rb") as f:
    data = pickle.load(f)

print("Type of top-level object:", type(data))

if isinstance(data, dict):
    print("\nTop-level keys:", list(data.keys()))
    for k, v in data.items():
        print(f"\nKey: {k!r}")
        print("  Type:", type(v))
        if hasattr(v, "shape"):
            print("  Shape:", v.shape)
        if hasattr(v, "columns"):
            print("  Columns:", list(v.columns))
        if isinstance(v, list):
            print("  Length:", len(v))
            print("  Sample:", v[:5])
else:
    print("Not a dict — attributes:", dir(data))