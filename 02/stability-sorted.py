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


# multiple sorts based on price ascending and weight descending order
sorted_product_list_price = sorted(product_list, key=lambda product: product.price)
sorted_product_list_price_weight = sorted(
    sorted_product_list_price, key=lambda product: product.weight, reverse=True
)
print(
    "sorted product list (price ascending, weight descending): ",
    sorted_product_list_price_weight,
)
