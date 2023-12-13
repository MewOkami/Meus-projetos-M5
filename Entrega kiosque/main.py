from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from menu import products
from management.tab_handler import calculate_tab
from management.product_handler import menu_report


if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(20))

    print(get_products_by_type("fruit"))

    new_products = {
        "title": "HamgurguerDelicia",
        "price": 75,
        "rating": 5,
        "description": "Melhor hamrguer Ever",
        "type": "fast-food"
    }

    print(add_product(products, **new_products))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    print(menu_report())

    ...
