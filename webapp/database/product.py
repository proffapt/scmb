from . import db
from typing import List
from models.product import *
from models.error import DB_Error
from models.shipment import Shipment
from database.shipment import delete_shipment, get_all_shipments_by_product


def get_all_products() -> List[Product] | DB_Error:
    try:
        products: List[Product] = Product.query.all()
        return products
    except Exception as e:
        return {"db_error": str(e)}


def get_product(code: str) -> Product | DB_Error:
    try:
        product: Product = Product.query.filter_by(code=code).first()
        if product:
            return product
        else:
            return {"db_error": "Product not found"}
    except Exception as e:
        return {"db_error": str(e)}


def create_product(code: str, name: str) -> Product | DB_Error:
    try:
        check_product: Product | DB_Error = get_product(code)
        if isinstance(check_product, Product):
            return {"db_error": "Product already exist"}
        else:
            product: Product = Product(code=code, name=name)
            db.session.add(product)
            db.session.commit()
            return product
    except Exception as e:
        return {"db_error": str(e)}


def update_product(code: str, name: str) -> Product | DB_Error:
    try:
        product: Product | DB_Error = get_product(code)
        if isinstance(product, Product):
            product.name = name
            db.session.commit()
            return product
        else:
            return product
    except Exception as e:
        return {"db_error": str(e)}


def delete_product(code: str) -> Product | DB_Error:
    try:
        product: Product | DB_Error = get_product(code)
        if isinstance(product, Product):
            # Delete the connected entries in Shipment table
            shipments: List[Shipment] | DB_Error = get_all_shipments_by_product(
                code)
            for shipment in shipments:
                if isinstance(shipment, Shipment):
                    delete_shipment(shipment.code)
            # Delete the product entry
            db.session.delete(product)
            # Commit the changes
            db.session.commit()
            return product
        else:
            return product
    except Exception as e:
        return {"db_error": str(e)}
