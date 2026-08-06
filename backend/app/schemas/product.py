from typing import Optional

from pydantic import BaseModel


class ProductResponse(BaseModel):

    id: int

    product_code: Optional[str] = None

    product_name: Optional[str] = None

    countries: Optional[str] = None

    categories: Optional[str] = None

    nutriscore_grade: Optional[str] = None

    nutriscore_score: Optional[int] = None

    nova_group: Optional[int] = None

    energy_kcal: Optional[float] = None

    fat: Optional[float] = None

    saturated_fat: Optional[float] = None

    carbohydrates: Optional[float] = None

    sugars: Optional[float] = None

    proteins: Optional[float] = None

    fiber: Optional[float] = None

    salt: Optional[float] = None

    sodium: Optional[float] = None

    class Config:
        from_attributes = True