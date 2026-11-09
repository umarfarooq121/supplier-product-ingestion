import json

def parse_supplier_b():
    with open(
        "feeds/supplier_b.json",
        "r",
        encoding="utf-8",
    ) as file:
        feed = json.load(file)
    
    return feed["products"]

if __name__ == "__main__":
    products = parse_supplier_b()
    print("Products loaded:", len(products))
    
    for product in products:
        print(product)
