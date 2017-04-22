# Product Inventory Management Practice - Classes

import random

class Product():
    def __init__(self, price, product_id, quantity):
        self.price = price
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = self.price * self.quantity

class Inventory():
    def __init__(self, products):
        self.inventory_value = 0
        self.products = list(products)

    def calculate_inventory_value(self):
        for index, product_object in enumerate(self.products):
            self.inventory_value += self.products[index].total_price
        print("Inventory Value: {}".format(self.inventory_value))

    def reset_inventory_value(self):
        self.inventory_value = 0

    def display_inventory(self):
        display_format_template = "\nItem {0}:\n\tProduct ID: {1}\n\tPrice: {2:.2f}\n\tQuantity: {3}\n\tTotal Price: {4}"
        for index, product_object in enumerate(self.products):
            print(display_format_template.format(index + 1, self.products[index].product_id, self.products[index].price, self.products[index].quantity, self.products[index].total_price))
        print("\n\tInventory Value: {:.2f}".format(self.inventory_value))

def generate_product_id(products):
    while generate_product_id:
        product_id = []
        product_id_sum = 0
        for digits in range(4):
            product_id.append(random.randint(1, 9))
        for digit in product_id:
            product_id_sum += digit
        product_id.append(product_id_sum)
        for index, digit in enumerate(product_id):
            product_id[index] = str(product_id[index])
        product_id = "".join(product_id)
        print(product_id)
        for index, product in enumerate(products):
            if any(product_id == products[index].product_id):
                print("breaking; product_id match")
                break
            else:
                print("breaking; no product_id match")
                yield product_id

def add_product(products):
    while add_product:
        value = input("How much does one unit cost?(USD): ")
        if value.isdigit():
            price = int(value)
            for stuff in generate_product_id(products):
                product_id = stuff
            print("Product ID: {:02d}".format(product_id))
        else:
            print("Invalid input")

products = []
add_product(products)

# products.append(Product(32.00, 167519, 10000))
# products.append(Product(50.00, 849324, 50000))

# products_inventory = Inventory(products)

# products_inventory.calculate_inventory_value()
# products_inventory.display_inventory()

# for index, product_object in enumerate(products):
#     print("Price of product index {}: {}".format(index, products[index].price))
#     product_sum += products[index].price
#     print(product_sum)
#     print(products[index].total_price)