class item:
    #Represents a shopping cart item.

    def __init__(self, item_name=None, item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        #Prints the total cost for this item (price * quantity) and returns it.
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")
        return cost