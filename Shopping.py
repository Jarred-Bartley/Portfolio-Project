from Item import item
from Read_number import read_number
from ShoppingCart import ShoppingCart
from datetime import date
#print menu function
def Print_menu():
    print("\n\n Menu: ")
    print("a. Add item to cart")
    print("b. Remove item from cart")
    print("c. Modify item in cart")
    print("d. View cart descriptions")
    print("f. View cart ")
    print("e. Exit")
    print("\nChoose an option: ")

def Menu():
    while True:
        Print_menu()
        choice = input().lower()
        if choice == 'a':
            print("Add item to cart")
            ShoppingCart.add_item(new_item())
        elif choice == 'b':
            print("Remove item from cart")
            ShoppingCart.remove_item(item_name())
        elif choice == 'c':
            print("Modify item in cart")
            ShoppingCart.modify_item(item_name())
        elif choice == 'd':
            print("View cart descriptions")
            ShoppingCart.print_descriptions()
        elif choice == 'f':
            print("view cart")
            ShoppingCart.print_total()
        elif choice == 'e':
            print("Exit")
            break
        else:
            print("Invalid option, please try again.")

def new_item():
    print("Enter the details of the item:")
    item_name = input("Item name: ")
    item_price = read_number("Item price: ")
    item_quantity = read_number("Item quantity: ")
    item_description = input("Item description: ")  
    return item(item_name, item_price, item_quantity , item_description)


def item_name():
    return input("Item name: ")

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


#MileStone 2:
print("\n\nWelcome to the shopping cart program!")
print("Name ?")
name = input()
today = date.today()
ShoppingCart = ShoppingCart(name, today)
Menu()

if __name__ == "__main__":
    main()