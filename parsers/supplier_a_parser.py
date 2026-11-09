import csv

def parse_supplier_a():
    with open(
        "feeds/supplier_a.csv",
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)
        products = list(reader)
    
    return products


if __name__ == "__main__":
    products = parse_supplier_a()
    print("Products loaded:", len(products))
    
    for product in products:
        print(product)