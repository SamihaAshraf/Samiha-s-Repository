#Samiha Ashraf
#1884227

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


if __name__ == "__main__":
    print("Item 1")
    itemA_name = input("Enter the item name:\n")
    itemA_price = float(input("Enter the item price:\n"))
    itemA_quantity = int(input("Enter the item quantity:\n"))
    itemA = ItemToPurchase(itemA_name, itemA_price, itemA_quantity)

    print("\nItem 2")
    itemB_name = input("Enter the item name:\n")
    itemB_price = float(input("Enter the item price:\n"))
    itemB_quantity = int(input("Enter the item quantity:\n"))
    itemB = ItemToPurchase(itemB_name, itemB_price, itemB_quantity)

    total_cost = itemA.item_quantity * itemA.item_price + itemB.item_quantity * itemB.item_price

    print("\nTOTAL COST")
    itemA.print_item_cost()
    itemB.print_item_cost()
    print(f"\nTotal: ${total_cost}")
