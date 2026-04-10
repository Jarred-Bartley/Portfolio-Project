class item:
    #A shopping cart item.

    def __init__(self, item_name=None, item_price=0.0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity) 
        self.item_description = str(item_description)

#Prints the total cost for this item (price * quantity) and returns it.
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")
        return cost
    
#Prints the item description.    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")