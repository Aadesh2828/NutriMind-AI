from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from app.core.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_code = Column(
        String(100),
        unique=True,
        index=True
    )

    product_name = Column(
        String(500),
        index=True
    )

    countries = Column(
        String
    )

    categories = Column(
        String
    )

    nutriscore_grade = Column(
        String(5)
    )

    nutriscore_score = Column(
        Integer
    )

    nova_group = Column(
        Integer
    )

    energy_kcal = Column(
        Float
    )

    fat = Column(
        Float
    )

    saturated_fat = Column(
        Float
    )

    carbohydrates = Column(
        Float
    )

    sugars = Column(
        Float
    )

    proteins = Column(
        Float
    )

    fiber = Column(
        Float
    )

    salt = Column(
        Float
    )

    sodium = Column(
        Float
    )

    created_at = Column(
        DateTime
    )