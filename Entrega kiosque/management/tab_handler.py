from menu import products


def calculate_tab(table):
    var_price = 0.0

    for t in table:
        resultTable = t["amount"]
        for p in products:
            if p["_id"] == t["_id"]:
                result = p["price"]
                multiplication = resultTable * result
                var_price += multiplication

    media_round = round(var_price, 2)

    final_result = f"${media_round}"

    return {"subtotal": final_result}
