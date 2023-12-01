'''
Aleksandra Mbuyi
Pramudya Wicaksono
Rei Onishi

Groceries Budgeting and Price Comparison Project
10/21/2023
'''

# Main Menu Interface
def menu_interface():
    print("Welcome to the Groceries Budget Program!".center(70))
    print("You can shop by the cheapest item across Walmart, Aldi and Target, add custom items or find average of an item!".center(70))
    print("Main Menu".center(70))
    print(" 1) Budget")
    print(" 2) Groceries")
    print(" 3) Budget-Cart Calculation")
    print(" 4) Quit")



# Groceries menu UI
def groceries_menu():
    print("---------------- Groceries ----------------")
    print(" 1) Shop Existing Items")
    print(" 2) Add New Items")
    print(" 3) Average price of Item")
    print(" 4) Quit")



# Budget menu UI
def budget_menu():
    print("--------------- Budget --------------------")
    print(" 1) Input Budget")
    print(" 2) Quit")



# Exit Program
def say_goodbye():
    print("Thank you for using our program! Goodbye!")



# Function below reads groceries.txt and then converts the file into a dictionary 
def txtconverter(price_data):
    with open('groceries.txt', 'r') as txtfile:
        # Read and skip the header line
        header = next(txtfile).strip().split('\t')
        
        # Iterate over each line in the TXT file
        for line in txtfile:
            # Split the line into columns based on the delimiter (e.g., '\t' for tab-separated)
            columns = line.strip().split('\t')
            
            # Extract item ID from the first column and convert it to an integer
            item_id = int(columns[0])
            
            # Create a dictionary for the current item
            item_dict = {"Item": columns[1]}
            
            # Extract and convert the values to float for 'Aldi', 'Target', and 'Walmart'
            for i in range(2, len(columns)):
                item_dict[header[i].strip()] = float(columns[i])
            
            # Add the item data to the price_data dictionary
            price_data[item_id] = item_dict



# Calculates how much of the budget is left after groceries.
def groceries_calculation(total_cart_cost, total_budget):
    
    #creates if statement when both cart and budget is greater than 0
    if total_cart_cost >= 0 and total_budget >= 0:
        groceries_calc = total_budget - total_cart_cost # Takes user's budget and subtracts total cost of cart.
        print("------------- Remaining Budget -------------------\n")
        print(f"Your Budget: ${total_budget}")
        print(f"Your Cart Cost: ${total_cart_cost:.2f}")
        print("____________________________________\n")
        if groceries_calc >= 0:
            print(f"You have ${groceries_calc:.2f} left on your budget\n")
        elif groceries_calc < 0:
            abs(groceries_calc)
            print(f"you are ${abs(groceries_calc):.2f} over budget.\n")



# Stores grocery items that the user selects in a list.
cart = []



# Shows user all of the pre-programmed groceries.
def show_list(price_data):
    print("---------------- Groceries ----------------")
    print("Available items:")
    for item_number, item_info in price_data.items():
        item_name = item_info["Item"]
        print(f"{item_number}: {item_name}")



# Shows user cart after they select groceries and quantity.
def show_cart(cart):
    global total_cart_cost # global allows us to change the value of total cart cost throughout the whole program.

    if cart:
        total_cart_cost = sum(item[2] for item in cart) # Sum of the total cost of each grocery item.

        print("Items in your cart from Target:")
        target_items = [item for item in cart if item[3] == 'Target'] # Identifies item's information, and sorts it into different stores - this one for Target.
        if target_items:
            for item in target_items:
                print(f"{item[1]} {item[0]}(s) for ${item[2]:.2f}") # Numbers in square brackets [] takes data from that position/index.
        else:
            print("no item from Target.\n")

        print("\nItems in your cart from Aldi:")
        aldi_items = [item for item in cart if item[3] == 'Aldi']
        if aldi_items:
            for item in aldi_items:
                print(f"{item[1]} {item[0]}(s) for ${item[2]:.2f}")
        else:
            print("no item from Aldi.\n")

        print("\nItems in your cart from Walmart:")
        walmart_items = [item for item in cart if item[3] == 'Walmart']
        if walmart_items:
            for item in walmart_items:
                print(f"{item[1]} {item[0]}(s) for ${item[2]:.2f}")
        else:
            print("no item from Walmart.\n")
        print(f"\nTotal Cart Cost: ${total_cart_cost:.2f}")
    else:
        print("cart is empty")



# Function to find the cheapest store for the specific grocery item after the user inputs the grocery item's ID number.
def find_cheapest_store(item_info):
    cheapest_store = None # Initialize cheapest_store.
    cheapest_price = float('inf')
    for store, price in item_info.items(): # Loops through and checks for the cheapest price and it's corresponding store.
        if store != "Item" and price < cheapest_price:
            cheapest_price = price
            cheapest_store = store
    return cheapest_store, cheapest_price

# Function that gets information from find_cheapest_store function and prints the item name, store, price, and quantity.
def calculate_cheapest_option(item_number, quantity):
    item_info = price_data.get(item_number)
    if item_info:
        item_name = item_info["Item"] # Establishes "Item" position within item_info.

        cheapest_store, cheapest_price = find_cheapest_store(item_info) # Calls find_cheapest_store function.
        print(f"{item_name} is cheapest at {cheapest_store} at ${cheapest_price:.2f}")

        quantity_valid = False
        while not quantity_valid: # Lets user input quantity and displays the total cost (quantity * cheapest_price)
            quantity_input = input(f"How many {item_name}(s) would you like to add to your cart? ")
            if quantity_input.isdigit():
                quantity = int(quantity_input)
                total_cost = cheapest_price * quantity
                cart.append((item_name, quantity, total_cost, cheapest_store))
                print(f"Added {quantity} {item_name}(s) to your cart from {cheapest_store} for ${total_cost:.2f}")
                quantity_valid = True
            else:
                print("Invalid input for quantity. Please enter a valid quantity.")
    else:
        print("Item not found in the database.")

# storesclass_py contains our class and methods, importing all methods and class.
from storesclass_py import *

# This is our tuple
grocery_stores = ("Target", "Aldi", "Walmart")

# Empty variables to allow loops to store information
total_budget = 0
total_cart_cost = 0

# To activate quit_program feature
quit_program = False

# Dictionary to store the list of items, price, stores converted from TXT file.
price_data = {}


while not quit_program: # Runs the loop
    txtconverter(price_data) # Calls TXT converter
    menu_interface()
    print(f'Your budget: {total_budget:.2f}\n')
    print(f'Your Cart Cost: {total_cart_cost:.2f}\n')
    main_menu_choice = int(input("Please enter choice with corresponding number:"))

    if main_menu_choice == 4:
        say_goodbye()
        quit_program = True # Ends the loop & terminates program.

    if main_menu_choice == 3:
        groceries_calculation(total_cart_cost, total_budget) 
        # Takes the total cart cost and the total budget, calls the function to calculate how much the user spent.

    elif main_menu_choice == 2:
        groceries_menu()
        groceries_choice = int(input("Please enter choice with corresponding number: "))
        if groceries_choice == 1:
            show_list(price_data)

            while True:
                print("Type 'exit' anytime you want to exit the program, 'done' when you are done adding yout list.")
                groceries_item_input = input("Please enter your choice of item with corresponding number:")
                
                if groceries_item_input.isnumeric() == True: # Creating an if statement when the input is numeric 
                    item_info = int(groceries_item_input)
                    calculate_cheapest_option(item_info, 0) # Calls function to calculate cheapest option, sets quantity to 0 intially.

                if groceries_item_input.lower() == "exit":
                    say_goodbye()
                    quit_program = True
                    break
                elif groceries_item_input.lower() == "done": # Breaks the loop and shows cart.
                    show_cart(cart)
                    break
                

        elif groceries_choice == 2:
            while True:
                print("type done when you are finish adding custom item to the cart")
                item_input = input("Item name:")
                if item_input.lower() == "done":                    
                    show_cart(cart)
                    print("Returning to main menu")
                    break  
                store_input = input("Store (T for Target, W for Walmart, A for Aldi:")
                new_item = Item(item_input, 0, 0, 0) # Instantiates class 'Item', passes item_input initially, sets the variables at 0 initally.
                
                if store_input == "T" or store_input == "t":
                    price_input = float(input("Price:"))
                    quantity_input = int(input("Input quantity:"))
                    new_item.set__Target_price(price_input) # Setters.
                    new_item.set__name(item_input)
                    total_cost = price_input * quantity_input
                    print(new_item)
                    cart.append((item_input, quantity_input, total_cost, "Target")) # Append function to add to cart list.
                    
                elif store_input == "W" or store_input == "w":
                    price_input = float(input("Price:"))
                    quantity_input = int(input("Input quantity:"))
                    new_item.set__Walmart_price(price_input)
                    new_item.set__name(item_input)
                    total_cost = price_input * quantity_input
                    print(new_item)
                    cart.append((item_input, quantity_input, total_cost, "Walmart"))
                    
                elif store_input == "A" or store_input == "a":
                    price_input = float(input("Price:"))
                    quantity_input = int(input("Input quantity:"))
                    new_item.set__Aldi_price(price_input)
                    new_item.set__name(item_input)
                    total_cost = price_input * quantity_input
                    print(new_item) # Calls string representation from class file.
                    cart.append((item_input, quantity_input, total_cost, "Aldi"))
                    

                
                    
        elif groceries_choice == 3:
            while True:
                show_list(price_data)
                avg_item_input = input("Please enter choice with corresponding number:")
                if avg_item_input.isnumeric() and int(avg_item_input) in price_data: # Creates an if statement where avg_item_input is a numerical input, converts it into interger. Must also be in price_data dictionary.
                    item_name = price_data[int(avg_item_input)]["Item"] # Stores item name in this variable.
                    average_price = Item.calculate_average_price(price_data[int(avg_item_input)]) # Calculates average price using the method in function.
                    print(f"The average price for {item_name} is: ${average_price:.2f}")
                    
                    another_item_input = input("Do you want to get the average price of another item? Type 'Y' for yes, or 'N' to go back to the main menu: ")
                    if another_item_input.upper() == "Y": # Loop to allow user to get average price for more than one item.
                        continue
                    elif another_item_input.upper() == "N":
                        break
                    else:
                        print("Invalid item. Please enter a valid item.")
                    pass

        elif groceries_choice == 4:
            say_goodbye()
            quit_program = True # Terminates program.

    elif main_menu_choice == 1:
        budget_menu()
        budget_choice = int(input("Please enter choice with corresponding number:"))
        if budget_choice == 1:
            print("Type 'exit' anytime you want to exit the program")
            budget_input = input("Please enter your budget:")
            if budget_input.replace(".", "").isnumeric(): # If statement that removes '.' where the input is numerical.
                budget_numeric = float(budget_input)
                total_budget = budget_numeric
                print(f"Budget is at ($): {total_budget:.2f}")

        elif budget_choice == 2:
            say_goodbye()
            quit_program = True
