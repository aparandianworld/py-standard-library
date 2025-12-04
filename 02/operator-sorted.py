from operator import attrgetter, itemgetter, methodcaller


class Product:
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.discount))

    def discount_price(self):
        return self.price - (self.price * self.discount)


product_list = [
    Product("Laptop", 1000, 10, 0.1),
    Product("Mouse", 25, 1, 0.05),
    Product("Keyboard", 50, 2, 0.02),
    Product("Monitor", 150, 3, 0.15),
    Product("Headphones", 75, 4, 0.08),
    Product("Webcam", 40, 5, 0.03),
    Product("USB Cable", 10, 6, 0.01),
    Product("Mousepad", 15, 10, 0.02),
    Product("Mousepad", 10, 11, 0.04),
    Product("Charger", 20, 11, 0.04),
    Product("Keyboard Mat", 25, 12, 0.02),
]

print("original product list: ", product_list)
print("---")
print(
    "sorted product list (price ascending)",
    sorted(product_list, key=attrgetter("price")),
)
print("---")
print(
    "sorted product list (price and weight ascending)",
    sorted(product_list, key=attrgetter("price", "weight")),
)
print("---")
print(
    "sorted product list (discount_price method)",
    sorted(product_list, key=methodcaller("discount_price")),
)

print("---")

inventory = [
    ("Widget 1", 10),
    ("Widget 2", 22),
    ("Widget 3", 13),
    ("Widget 4", 44),
    ("Widget 5", 5),
]

print(
    "sorted inventory based on number of products", sorted(inventory, key=itemgetter(1))
)
print(
    "sorted inventory based on number of products",
    sorted(inventory, key=lambda item: item[1]),
)
