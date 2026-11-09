def create_product(
    supplier,
    source_id,
    name,
    category,
    price,
    currency,
    stock,
):
    return {
        "supplier": supplier,
        "source_id": source_id,
        "name": name,
        "category": category,
        "price": price,
        "currency": currency,
        "stock": stock,
    }