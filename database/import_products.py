import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


# --------------------------------------------------
# 1. Find Project Root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# 2. Load .env from backend folder
# --------------------------------------------------

ENV_FILE = PROJECT_ROOT / "backend" / ".env"

load_dotenv(ENV_FILE)


# --------------------------------------------------
# 3. Get Database URL
# --------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        f"DATABASE_URL is not configured. "
        f"Please check your .env file at: {ENV_FILE}"
    )


# --------------------------------------------------
# 4. Create PostgreSQL Connection
# --------------------------------------------------

engine = create_engine(DATABASE_URL)


# --------------------------------------------------
# 5. CSV File Path
# --------------------------------------------------

CSV_PATH = PROJECT_ROOT / "data" / "processed" / "open_food_facts.csv"


# --------------------------------------------------
# 6. Read CSV
# --------------------------------------------------

print("Reading CSV file...")
print(f"CSV location: {CSV_PATH}")

df = pd.read_csv(CSV_PATH)

print(f"Total records found: {len(df)}")


# --------------------------------------------------
# 7. Rename Columns
# --------------------------------------------------

df = df.rename(
    columns={
        "code": "product_code",
        "clean_name": "product_name",
        "countries_tags": "countries",
        "categories_tags": "categories",
    }
)


# --------------------------------------------------
# 8. Select Required Columns
# --------------------------------------------------

columns = [
    "product_code",
    "product_name",
    "countries",
    "categories",
    "nutriscore_grade",
    "nutriscore_score",
    "nova_group",
    "energy_kcal",
    "fat",
    "saturated_fat",
    "carbohydrates",
    "sugars",
    "proteins",
    "fiber",
    "salt",
    "sodium",
]

df = df[columns]


# --------------------------------------------------
# 9. Convert Empty Strings to NULL
# --------------------------------------------------

df = df.replace(r"^\s*$", None, regex=True)


# --------------------------------------------------
# 10. Upload to PostgreSQL
# --------------------------------------------------

print("Uploading data to PostgreSQL...")

df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000,
    method="multi",
)


# --------------------------------------------------
# 11. Success Message
# --------------------------------------------------

print("===================================")
print("Data import completed successfully!")
print(f"Records imported: {len(df)}")
print("===================================")