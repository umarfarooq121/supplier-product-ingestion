from parsers.supplier_a_parser import parse_supplier_a
from parsers.supplier_b_parser import parse_supplier_b

from normalisers.supplier_a_normaliser import normalise_supplier_a
from normalisers.supplier_b_normaliser import normalise_supplier_b



def main():
    supplier_a_products = parse_supplier_a()
    supplier_b_products = parse_supplier_b()

    all_products = []

    for product in supplier_a_products:
        normalised_product = normalise_supplier_a(product)
        all_products.append(normalised_product)

    for product in supplier_b_products:
        normalised_product = normalise_supplier_b(product)
        all_products.append(normalised_product)

    print("Total products loaded:", len(all_products))

    for product in all_products:
        print(product)


if __name__ == "__main__":
    main()