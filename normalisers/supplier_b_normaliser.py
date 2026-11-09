from normalisers.product_model import create_product
from decimal import Decimal

def normalise_supplier_b(product):
    return create_product(
        supplier="supplier_b",
        source_id=product["product_code"],
        name=product["name"],
        category=product["product_category"],
        price=Decimal(str(product["unit_price"])),
        currency=product["currency_code"],
        stock=int(product["quantity_available"]),
    )
    