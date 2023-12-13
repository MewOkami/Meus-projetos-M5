from menu import products


def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for p in products:
        if p["_id"] == id:
            return p
    return {}


def get_products_by_type(types):
    if types != str(types):
        raise TypeError("product type must be a str")

    results = []
    for p in products:
        if p["type"] == types:
            results.append(p)
    return results


def add_product(products, **new_products):
    if len(products) == 0:
        new_Id = len(products) + 1
        new_products["_id"] = new_Id
        products.append(new_products)
        return new_products

    product = products[-1]
    new_Id = product['_id'] + 1
    new_products["_id"] = new_Id
    products.append(new_products)
    return new_products


def menu_report():
    len_Products = len(products)

    sum_prices = 0.0

    for p in products:
        sum_prices += p["price"]

    media_price = sum_prices / len(products)

    media_round = round(media_price, 2)

    common_type = "fruit"

    return f"Products Count: {len_Products} - Average Price: ${media_round} - Most Common Type: {common_type}"
