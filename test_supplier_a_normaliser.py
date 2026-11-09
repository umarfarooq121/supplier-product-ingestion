from parsers.supplier_a_parser import parse_supplier_a
from normalisers.supplier_a_normaliser import normalise_supplier_a


products = parse_supplier_a()

for product in products:
    normalised_product = normalise_supplier_a(product)
    print(normalised_product)