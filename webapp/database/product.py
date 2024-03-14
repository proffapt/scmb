from models import Product
from typing import List


def get_all_products() -> List[Product]:
    return [
        {
            "code": "#45BHJ",
            "name": "Mango"
        },
        {
            "code": "#47BHJ",
            "name": "Apple"
        }
    ]


def get_product(code: str) -> Product:
    return {
        "code": code,
        "name": "Mango"
    }


def create_or_update_product(code: str, name: str) -> Product:
    return {
        "code": code,
        "name": name
    }


def delete_product(code: str) -> Product:
    return {
        "code": code,
        "name": "Mango"
    }
