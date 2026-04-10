from Item import item
from Read_number import read_number
def main():
#item 1
   print("Enter the details of the first item:")
   item_name = input("Item name: ")
   item_price = read_number("Item price: ")
   item_quantity = read_number("Item quantity: ")
   a = item(item_name, item_price, item_quantity)
   
#item 2
   print("\nEnter the details of the second item:")
   item_name = input("Item name: ") 
   item_price = read_number("Item price: ")
   item_quantity = read_number("Item quantity: ")
   b = item(item_name, item_price, item_quantity)
   
#tota cost
   a.print_item_cost()
   b.print_item_cost() 
   total_cost = a.item_price * a.item_quantity + b.item_price * b.item_quantity
   print("\nTotal cost: $", round(total_cost, 2))

if __name__ == "__main__":
    main()