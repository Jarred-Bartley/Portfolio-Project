from Item import item
from Read_number import read_number

class ShoppingCart:
    #A shopping cart.
    
    def __init__(self, customer_name=None, current_date=None):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
        self.cart_items = []

    #Adds an item to the shopping cart.    
    def add_item(self, item):
       
        self.cart_items.append(item)

    #Removes an item from the shopping cart. If the item was not found, prints a message.    
    def remove_item(self, item_name):
        
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")
        
    #Modifies an item in the shopping cart. If the item was not found, prints a message.    
    def modify_item(self, item_name):
        
        for i, existing_item in enumerate(self.cart_items):
            if existing_item.item_name == item_name:
                itemTopurchase = item(existing_item.item_name, existing_item.item_price, existing_item.item_quantity, existing_item.item_description)
                new_price = read_number("Enter new price (or -1 to keep current price): ")
                if new_price != -1:
                    itemTopurchase.item_price = new_price
                new_quantity = read_number("Enter new quantity (or -1 to keep current quantity): ") 
                if new_quantity != -1:
                    itemTopurchase.item_quantity = new_quantity
                new_description = input("Enter new description (or leave blank to keep current description): ")
                if new_description.strip() != "":
                    itemTopurchase.item_description = new_description
                self.cart_items[i] = itemTopurchase 
                return
        print("Item not found in cart. Nothing modified.")

    #Returns the number of items in the shopping cart.
    def get_num_items_in_cart(self):
        
        return sum(item.item_quantity for item in self.cart_items)
    
    #Returns the total cost of the items in the shopping cart.
    def get_cost_of_cart(self):
        
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    #Prints the total cost of the items in the shopping cart.
    def print_total(self):
        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")
    #Prints the descriptions of the items in the shopping cart.
    def print_descriptions(self):
        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()