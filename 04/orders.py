import json


def calculate_orders(orders):
    result = 0

    if orders == "":
        print("Error: orders is empty")
        return

    orders_obj = json.loads(orders)
    for order in orders_obj["orders"]:
        result += order["amount"]
    return result


def main():
    orders = """{
    "company":"ACME Inc.",
    "orders" : [
        {"product":"Widget A","amount":255.0},
        {"product":"Widget B","amount":125.50},
        {"product":"Widget C","amount":85.75},
        {"product":"Widget D","amount":413.25}
    ]
}
"""
    sum_orders = calculate_orders(orders)
    print("Sum of orders: ", sum_orders)


if __name__ == "__main__":
    main()
