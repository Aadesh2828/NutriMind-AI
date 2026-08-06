from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductResponse


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get(
    "/",
    response_model=List[ProductResponse]
)
def get_products(
    limit: int = Query(
        default=20,
        ge=1,
        le=100
    ),
    db: Session = Depends(get_db)
):

    products = (
        db.query(Product)
        .limit(limit)
        .all()
    )

    return products


@router.get(
    "/search",
    response_model=List[ProductResponse]
)
def search_products(
    query: str,
    limit: int = Query(
        default=20,
        ge=1,
        le=100
    ),
    db: Session = Depends(get_db)
):

    products = (
        db.query(Product)
        .filter(
            Product.product_name.ilike(
                f"%{query}%"
            )
        )
        .limit(limit)
        .all()
    )

    return products


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(Product)
        .filter(
            Product.id == product_id
        )
        .first()
    )

    return product