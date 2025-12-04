class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.discount))

    def discount_price(self):
        return self.price - (self.price * self.discount)


product_list = [
    Product("Laptop", 1000, 0.1),
    Product("Mouse", 25, 0.05),
    Product("Keyboard", 50, 0.02),
    Product("Monitor", 150, 0.15),
    Product("Headphones", 75, 0.08),
    Product("Webcam", 40, 0.03),
    Product("USB Cable", 10, 0.01),
    Product("Mousepad", 15, 0.02),
    Product("Charger", 20, 0.04),
    Product("Keyboard Mat", 25, 0.02),
]

print("original product list: ", product_list)


def product_sort(product):
    return product.price


print("sorted product list (key is price)", sorted(product_list, key=product_sort))

print(
    "sorted product list (key is product name)",
    sorted(product_list, key=lambda product: product.name),
)

# notice you can sort based on object method as well
print(
    "sorted product list (key is discount price)",
    sorted(product_list, key=lambda product: product.discount_price()),
)
