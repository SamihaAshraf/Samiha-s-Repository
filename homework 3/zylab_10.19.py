#Samiha Ashraf
#1884227

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}\n")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_quantity * item.item_price for item in self.cart_items)
        return total_cost

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY\n")

        for item in self.cart_items:
            item.print_item_cost()

        print("Total:", "$" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


# Main section
if __name__ == "__main__":
    # Prompt for customer's name
    customer_name = input("Enter customer's name:\n")

    # Prompt for today's date
    current_date = input("Enter today's date:")

    # Output customer name and today's date
    print("\n")
    print("Customer name:", customer_name)
    print("Today's date:", current_date)

    def display_menu():
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")

    def print_menu(cart):
        running = True
        display_menu()
        while running:
            choice = input("Choose an option:\n")

            if choice == 'a':
                add_item_to_cart(cart)
                display_menu()
            elif choice == 'r':
                remove_item_from_cart(cart)
                display_menu()
            elif choice == 'c':
                change_item_quantity(cart)
                display_menu()
            elif choice == 'i':
                cart.print_descriptions()
                display_menu()
            elif choice == 'o':
                cart.print_total()
                display_menu()
            elif choice == 'q':
                running = False
            else:
                choice = input("Choose an option:\n")

    def add_item_to_cart(cart):
        print("\nADD ITEM TO CART")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(item)

    def remove_item_from_cart(cart):
        print("\nREMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        cart.remove_item(item_name)

    def change_item_quantity(cart):
        print("\nCHANGE ITEM QUANTITY")
        item_name = input("Enter the item name:\n")
        new_quantity = int(input("Enter the new quantity:\n"))
        item = ItemToPurchase()
        item.item_name = item_name
        item.item_quantity = new_quantity
        cart.modify_item(item)

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)
