# Product Inventory Management Practice - Classes
# Add exit on demand

import random

class Product():
    def __init__(self, price, product_id, quantity):
        self.price = float(price)
        self.product_id = str(product_id)
        self.quantity = int(quantity)
        self.total_price = self.price * self.quantity

class Inventory():
    def __init__(self, products):
        self.products = list(products)
        self.inventory_value = 0
        for index, product_object in enumerate(self.products):
            self.inventory_value += self.products[index].total_price

    def display_inventory(self):
        """
        Sets a string as the template for the formatting of the inventory display. It iterates through the 'products' list and displays the product's information using the template. The template is used to avoid clutter in the print statement.
        """
        if len(self.products) == 0:
            print("\nInventory is empty.")
            return
        display_format_template = "\nItem {0}:\n\tProduct ID: {1}\n\tPrice: {2:.2f}\n\tQuantity: {3}\n\tTotal Price: {4:.2f}"
        for index, product_object in enumerate(self.products):
            print(display_format_template.format(index + 1, self.products[index].product_id, self.products[index].price, self.products[index].quantity, self.products[index].total_price))
        print("\n\tInventory Value: {:.2f}".format(self.inventory_value))

def generate_product_id(products):
    """Generates a new product id for a new product being added/created. 'Randomly' generates 4 digits from 1-9 and appends its (the 4 digits individually) sum, so '1111' would get changed to '11114'. It then iterates through the new id and changes each digit (element) to a string. The list is then changed to a single string. It then gets offloaded to get validated (the new id).
    """
    while generate_product_id:
        new_product_id = []
        product_id_sum = 0
        [new_product_id.append(random.randint(1, 9)) for digits in range(4)]
        for digit in new_product_id:
            product_id_sum += digit
        new_product_id.append(product_id_sum)
        for index, digit in enumerate(new_product_id):
            new_product_id[index] = str(new_product_id[index])
        new_product_id = "".join(new_product_id)
        return validate_product_id(products, new_product_id)

def validate_product_id(products, new_product_id):
    """
    Checks for validity of newly generated product id. Iterates through the product objects in 'products' list and checks if the new id matches an id from one of the products. If invalid, a new id is generated (product id generating function is called again/returned to).
    
    It also checks the length of the new id, if it's less than 6; so the sum of the first 4 generated values for the id is less than 10. It inserts a '0' to just before the last digit.
    """
    for index, product in enumerate(products):
        if new_product_id == products[index].product_id:  
            return generate_product_id(products)
    if len(new_product_id) < 6:
        new_product_id_list = list(new_product_id)
        new_product_id_list.insert(len(new_product_id_list) - 1, "0")
        new_product_id = "".join(new_product_id_list)
    return new_product_id

def add_product(products):
    while add_product:
        price_ask = input("\nHow much does one unit cost?(USD): ")
        quantity_ask = input("How many units of it are available?: ")
        if price_ask.isdigit() and quantity_ask.isdigit():
            price = float(price_ask)
            quantity = int(quantity_ask)
            product_id = generate_product_id(products)
            print("\nProduct Information:\n\tProduct ID: {0}\n\tPrice: {1:.2f}\n\tQuantity: {2}".format(product_id, price, quantity))
            sure = str.lower(input("Are you sure that these are correct?(y/n): "))
            if sure == 'y':
                products.append(Product(price, product_id, quantity))
                products_inventory = Inventory(products) # Overwrites any previous inventories so that it's updated.
                return products_inventory
            elif sure == 'n':
                continue
            else:
                input_error()
                continue
        else:
            input_error()

def delete_product(products):
    while delete_product:
        products_inventory.display_inventory()
        choice = input("\nWhich product would you like to delete?: ")
        if choice.isdigit():
            if choice > len(products) or choice <= 0:
                input_error()
                continue
            sure = input("\nAre you sure?(y/n): ")
            if sure == 'y':
                del products[len(products) - 1] # Deletes the product object
            elif sure == 'n':
                continue
            else:
                input_error()
                continue
        else:
            input_error()

def input_error():
    print("\nInvalid input.")

products = []
products_inventory = Inventory(products)
active = True

print("\nWelcome new manager!\n\nPlease note that product IDs are generated automatically, so don't be alarmed when you see it without you having to set it!\nRemember, you can always say 'q' to quit the command you're being asked to commit!")

while active:
    command = input("\nWhat would like to do?\n\t1. Add product to inventory\n\t2. Delete product from inventory\n\t3. Edit product in inventory\n\t4. Display inventory\n")
    if command == '1':
        products_inventory = add_product(products)
    elif command == '2':
        products_inventory = delete_product(products) # Implement this
    elif command == '3':
        products_inventory = edit_product(products) # Implement this
    elif command == '4':
        products_inventory.display_inventory()
    elif command == 'q':
        print("\nExitting Program...")
        break
    else:
        input_error()
        

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
