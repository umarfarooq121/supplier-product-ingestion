from decimal import Decimal
from normalisers.product_model import create_product

def normalise_supplier_a(product):
    return [
        create_product(
        supplier="supplier_a",
        source_id=product["sku"],
        name=product["product_name"],
        category=product["category"],
        price=Decimal(product["price"]),
        currency=product["currency"],
        stock=int(product["stock"]),
    )
    ]