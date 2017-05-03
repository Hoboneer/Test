# Product Inventory Management Practice - Classes

import random

class Product():
    def __init__(self, price, product_id, quantity):
        self.price = float(price)
        self.product_id = str(product_id)
        self.quantity = int(quantity)
        self.total_price = self.price * self.quantity

    def update_product(self, price, quantity):
        self.price = float(price)
        self.quantity = int(quantity)
        self.total_price = self.price * self.quantity

class Inventory():
    def __init__(self):
        self.products = []
        self.inventory_value = 0

    def display_inventory(self):
        """
        Sets a string as the template for the formatting of the inventory 
        display. It iterates through the 'products' list and displays the
        product's information using the template. The template is used to 
        avoid clutter in the print statement.
        """
        self.update_inventory_value()
        if len(self.products) == 0:
            print("\nInventory is empty.")
            return
        display_format_template = "\nItem {0}:\n\tProduct ID: {1}\n\tPrice: ${2:.2f}\n\tQuantity: {3}\n\tTotal Price: ${4:.2f}"
        for index, product_object in enumerate(self.products):
            print(display_format_template.format(index + 1, self.products[index].product_id, self.products[index].price, self.products[index].quantity, self.products[index].total_price))
        print("\n\tInventory Value: ${:.2f}".format(self.inventory_value))

    def update_inventory_value(self):
        """
        Updates the (total) inventory value. It resets it to '0' first and
        iterates over the enumeration of the 'self.products' list, adding the
        total price of the products it iterates over to the inventory value. 
        This method is called only by 'display_inventory()' to keep an updated 
        display.
        """
        self.inventory_value = 0
        for index, product_object in enumerate(self.products):
            self.inventory_value += self.products[index].total_price

    def add_product(self):
        """
        Asks user the price and the quantity of the units of the product.
        Validity checks and affirmation checks happen.
        Upon success of the whole method, it appends the specified product
        object to the list in the (one) instance of 'Inventory'.
        """
        while self.add_product:
            price_ask = str.lower(input("\nHow much does one unit cost?(USD): "))
            quantity_ask = str.lower(input("How many units of it are available?: "))
            if price_ask.isdigit() and quantity_ask.isdigit():
                price = float(price_ask)
                quantity = int(quantity_ask)
                product_id = generate_product_id()
                print("\nProduct Information:\n\tProduct ID: {0}\n\tPrice: ${1:.2f}\n\tQuantity: {2}".format(product_id, price, quantity))
                sure = str.lower(input("Are you sure that these are correct?(y/n): "))
                if sure == 'y':
                    self.products.append(Product(price, product_id, quantity))
                    return
                elif sure == 'n':
                    continue
                elif sure == 'q':
                    quit_current_menu()
                    return
                else:
                    input_error()
                    continue
            elif price_ask or quantity_ask == 'q':
                quit_current_menu()
                return
            else:
                input_error()
                continue

    def delete_product(self):
        """
        Asks user which product they would like to delete, a bunch of 
        validation checks and affirmation checks. Upon success of the whole 
        method, it deletes the product that the user chose.
        """
        while self.delete_product:
            products_inventory.display_inventory()
            if len(self.products) == 0:
                return
            choice = str.lower(input("\nWhich product would you like to delete?: "))
            if choice.isdigit():
                if int(choice) > len(self.products) or int(choice) <= 0:
                    input_error()
                    continue
                sure = input("\nAre you sure?(y/n): ")
                if sure == 'y':
                    del products_inventory.products[int(choice) - 1]
                    print("\nItem {} deleted.".format(choice))
                    return
                elif sure == 'n':
                    continue
                elif sure == 'q':
                    quit_current_menu()
                    return
                else:
                    input_error()
                    continue
            elif choice == 'q':
                quit_current_menu()
                return
            else:
                input_error()
                continue

    def edit_product(self):
        """
        Asks user which product they would like to edit then asks the price of 
        one unit and the quantity of units. Upon success of the whole method, 
        it overwrites the old product with a new one.
        """
        while self.edit_product:
            products_inventory.display_inventory()
            if len(self.products) == 0:
                return
            choice = str.lower(input("Which product would you like to edit?: "))
            if choice.isdigit():
                if int(choice) > len(self.products) or int(choice) <= 0:
                    input_error()
                    continue
                sure = input("\nAre you sure?(y/n): ")
                while sure == 'y':
                    price_ask = str.lower(input("\nHow much does one unit cost?(USD): "))
                    quantity_ask = str.lower(input("How many units of it are available?: "))
                    new_id_ask = str.lower(input("Do you want to generate a new ID for this product?(y/n): "))
                    if price_ask.isdigit() and quantity_ask.isdigit() and new_id_ask == 'y' or new_id_ask == 'n':
                        price = float(price_ask)
                        quantity = int(quantity_ask)
                        product_id = self.products[int(choice) - 1].product_id
                        if new_id_ask == 'y':
                            product_id = generate_product_id()
                        print("\nProduct Information:\n\tProduct ID: {0}\n\tPrice: ${1:.2f}\n\tQuantity: {2}".format(product_id, price, quantity))
                        sure = str.lower(input("Are you sure that these are correct?(y/n): "))
                        if sure == 'y':
                            self.products[int(choice) - 1].update_product(price, quantity)
                            return
                        elif sure == 'n':
                            continue
                        elif sure == 'q':
                            quit_current_menu()
                            return
                        else:
                            input_error()
                            continue
                    elif price_ask or quantity_ask or new_id_ask == 'q':
                        quit_current_menu()
                        return
                    else:
                        input_error()
                        continue
                if sure == 'n':
                    continue
                elif sure == 'q':
                    quit_current_menu()
                    return
                else:
                    input_error()
                    continue
            if choice == 'q':
                quit_current_menu()
                return
            else:
                input_error()
                continue


def generate_product_id():
    """
    Generates a new product id for a new product being added/created. 
    'Randomly' generates 4 digits from 1-9 and appends its (the 4 digits 
    individually) sum, so '1111' would get changed to '11114'. It then 
    iterates through the new id and changes each digit (element) to a string. 
    The list is then changed to a single string. It then gets offloaded to get 
    validated (the new id).
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
        return validate_product_id(products_inventory, new_product_id)

def validate_product_id(products_inventory, new_product_id):
    """
    Checks for validity of newly generated product id. Iterates through the 
    product objects in 'products' list and checks if the new id matches an id 
    from one of the products. If invalid, a new id is generated (product id 
    generating function is called again/returned to).
    
    It also checks the length of the new id, if it's less than 6; so the sum 
    of the first 4 generated values for the id is less than 10. It inserts a 
    '0' to just before the last digit.
    """
    for index, product in enumerate(products_inventory.products):
        if new_product_id == products_inventory.products[index].product_id:  
            return generate_product_id()
    if len(new_product_id) < 6:
        new_product_id_list = list(new_product_id)
        new_product_id_list.insert(len(new_product_id_list) - 1, "0")
        new_product_id = "".join(new_product_id_list)
    return new_product_id

def input_error():
    """
    Outputs error message when user enters an input not available to be used 
    by the program at that point in time. The function it's called by then 
    continues to the next iteration using 'continue'.
    """
    print("\nInvalid input.")

def quit_current_menu():
    """
    Tells user that it is quitting out of the current command menu, the 
    function it's called by then returns to the main loop. Triggered by the 
    user typing 'q'.
    """
    print("\nQuitting current command menu...")

products_inventory = Inventory()
active = True

print("\nWelcome new manager!\n\nPlease note that product IDs are generated automatically, so don't be alarmed when you see it without you having to set it!\nRemember, you can always say 'q' to quit the command you're being asked to commit!")

while active:
    command = str.lower(input("\nWhat would like to do?\n\t1. Add product to inventory\n\t2. Delete product from inventory\n\t3. Edit product in inventory\n\t4. Display inventory\n"))
    if command == '1':
        products_inventory.add_product()
    elif command == '2':
        products_inventory.delete_product()
    elif command == '3':
        products_inventory.edit_product()
    elif command == '4':
        products_inventory.display_inventory()
    elif command == 'q':
        print("\nExitting Program...")
        break
    else:
        input_error()
        continue
