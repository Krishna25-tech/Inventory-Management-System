class Item:
    def __init__(self, name, price, quantity, item_id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.item_id = item_id

    def add_stock(self, units):
        if units <= 0:
            return False

        self.quantity += units
        return True


    def remove_stock(self, units):
        if units <= 0:
            return False
        if units > self.quantity:
            return False
        self.quantity -= units
        return True

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self,item):
        self.items[item.item_id] = item


    def menu(self):
      while True:
        for item in self.items.values():
            print("Name :",item.name, "Price :",item.price, "Quantity :",item.quantity,"Product ID:", item.item_id)

        user_input = input("Enter item ID to select (or q to exit): ")

        if user_input.lower() == "q":
            break

        try:
            item_id = int(user_input)
        except ValueError:
            print("Enter a valid numeric item ID.")
            continue
        if item_id not in self.items:
            print("Item not found.")
            continue
        item = self.items[item_id]

        while True:
            print("1. Restock")
            print("2. Sell")
            print("3. Check quantity")
            print("4. Back to item list")

            choice = input("Enter your choice: ")

            if choice == "1":
                try :
                    units = int(input("Enter number of units to be added: "))
                except ValueError:
                    print("Enter a valid numeric number of units.")
                    continue
                if item.add_stock(units):
                    print("Successfully added.")
                else :
                    print("Failed to add.")

            elif choice == "2":
                try :
                    units = int(input("Enter number of units to be removed: "))
                except ValueError:
                    print("Enter a valid numeric number of units.")
                    continue
                if item.remove_stock(units):
                    print("Successfully removed.")
                else :
                    print("Failed to remove.")

            elif choice == "3":
                print("Quantity : " + str(item.quantity))

            elif choice == "4":
                break

            else :
                print("Enter a valid choice.")

item1 = Item("Chips", 10, 10, 1)
item2 = Item("Biscuit", 30, 40, 2)
item3 = Item("Burger", 69, 15, 3)

inv = Inventory()
inv.add_item(item1)
inv.add_item(item2)
inv.add_item(item3)
inv.menu()




