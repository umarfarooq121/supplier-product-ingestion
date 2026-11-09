from parsers.supplier_b_parser import parse_supplier_b
from normalisers.supplier_b_normaliser import normalise_supplier_b

products = parse_supplier_b()

for product in products:
    normalised_product = normalise_supplier_b(product)
    print(normalised_product)