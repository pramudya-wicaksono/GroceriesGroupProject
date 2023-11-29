# -*- coding: utf-8 -*-
"""Group_Project_Groceries.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1umZOb8SgQ1YPLty3fxiXwYJBZm9weqFE
"""

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
    print("You can shop by the cheapest item by store or choose to shop at one store!".center(70))
    print("Main Menu".center(70))
    print(" 1) Budget")
    print(" 2) Groceries")
    print(" 3) Budget-Cart Calculation")
    print(" 4) Quit")

def budget_cart_calc():
    print("Budget-Cart Calculation Menu".center(70))
    print(" 1) Calculate How your Budget ")

# Groceries menu
def groceries_menu():
    print("---------------- Groceries ----------------")
    print(" 1) Shop Existing Items")
    print(" 2) Add New Items")
    print(" 3) Average price of Item")
    print(" 4) Quit")


        
        


# Budget menu
def budget_menu():
    print("--------------- Budget --------------------")
    print(" 1) Input Budget")
    print(" 2) Quit")

def say_goodbye():
    print("Thank you for using our program! Goodbye!")

def write_cart_to_file(cart):
    file = open("cart_details.txt", "w")
    if file:
        file.write("Your Cart:\n")
        total_cart_cost = 0
        for item in cart:
            item_name, quantity, total_cost, cheapest_store = item
            file.write(f"{item_name} ({cheapest_store}): {quantity} items - ${total_cost:.2f}\n")
            total_cart_cost += total_cost
        file.write(f"Total Cart Cost: ${total_cart_cost:.2f}\n")
        print("Cart details have been written to 'cart_details.txt'.")
        file.close()
    else:
        print("Error opening the file. Check file path and permissions.")

def txtconverter(price_data):
    with open('groceries.txt', 'r') as txtfile:
        # Read the header line
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

def groceries_calculation(total_cart_cost, total_budget):
    # Would not read total_cart_cost
    if total_cart_cost > 0 and total_budget > 0:
        groceries_calc = total_budget - total_cart_cost
        print("------------- Remaining Budget -------------------\n")
        print(f"Your Budget: ${total_budget}")
        print(f"Your Cart Cost: ${total_cart_cost}")
        print("____________________________________\n")
        if groceries_calc >= 0:
            print(f"You have ${groceries_calc} left on your budget\n")
        elif groceries_calc < 0:
            abs(groceries_calc)
            print(f"you are ${groceries_calc} over budget.\n")

cart = []
# How would the function know which one is 'store' in the dictionary?
# What is inf on 'cheapest_price = float('inf')'?
# Function to calculate the cheapest option and total cost
def show_list(price_data):
    print("---------------- Groceries ----------------")
    print("Available items:")
    for item_number, item_info in price_data.items():
        item_name = item_info["Item"]
        print(f"{item_number}: {item_name}")

def show_cart(cart):
    global total_cart_cost

    if cart:
        total_cart_cost = sum(item[2] for item in cart)

        print("Items in your cart from Target:")
        target_items = [item for item in cart if item[3] == 'Target']
        if target_items:
            for item in target_items:
                print(f"{item[1]} {item[0]}(s) for ${item[2]:.2f}")
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
        print(f"Total Cart Cost: ${total_cart_cost:.2f}")
    else:
        print("cart is empty")


def show_list_by_store():
    for id in price_data:
        print(f"{id})", price_data[id].get_name())

def find_cheapest_store(item_info):
    cheapest_store = None
    cheapest_price = float('inf')
    for store, price in item_info.items():
        if store != "Item" and price < cheapest_price:
            cheapest_price = price
            cheapest_store = store
    return cheapest_store, cheapest_price

def calculate_cheapest_option(item_number, quantity):
    item_info = price_data.get(item_number)
    if item_info:
        item_name = item_info["Item"]

        cheapest_store, cheapest_price = find_cheapest_store(item_info)
        print(f"{item_name} is cheapest at {cheapest_store} at ${cheapest_price:.2f}")

        quantity_valid = False
        while not quantity_valid:
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

from storesclass_py import Item
grocery_stores = ("Target", "Aldi", "Walmart")
total_budget = 0
total_cart_cost = 0
quit_program = False
price_data = {}
groceries_by_store = []
while not quit_program:
    txtconverter(price_data)
    menu_interface()
    print(f'this is budget {total_budget}\n')
    print(f'this is groceries {total_cart_cost}\n')
    main_menu_choice = int(input("Please enter choice with corresponding number:"))

    if main_menu_choice == 4:
        say_goodbye()
        quit_program = True

    if main_menu_choice == 3:
        groceries_calculation(total_cart_cost, total_budget)

    elif main_menu_choice == 2:
        groceries_menu()
        groceries_choice = int(input("Please enter choice with corresponding number:"))
        if groceries_choice == 1:
            show_list(price_data)

            while True:
                print("Type 'exit' anytime you want to exit the program, 'done' when you are done adding yout list.")
                groceries_item_input = input("Please enter your choice of item with corresponding number:")
                if groceries_item_input.isnumeric() == True:
                    item_info = int(groceries_item_input)
                    calculate_cheapest_option(item_info, 0)

                if groceries_item_input.lower() == "exit":
                    say_goodbye()
                    quit_program = True
                    break
                elif groceries_item_input.lower() == "done":
                    show_cart(cart)
                    break

        elif groceries_choice == 2:
            while True:
                print("type done when you are finish adding custom item to the cart")
                item_input = input("Item name:")
                store_input = input("Store (T for Target, W for Walmart, A for Aldi:")
                if store_input.lower() == "T":
                    #put getters for Target here
                    price_input = float(input("Price:"))
                    pass
                elif store_input.lower() == "W":
                    #put getters for Walmart here
                    price_input = float(input("Price:"))
                    pass
                elif store_input.lower() == "A":
                    #put getters for Aldi here
                    price_input = float(input("Price:"))
                    pass
                elif store_input.lower() == "done":
                    break
                    
        elif groceries_choice == 3:
            show_list(price_data)
            while True:
                avg_item_input = int(input("Please enter choice with corresponding number"))
                if avg_item_input.isnumeric():
                    #put average calculation here
                    pass
                # PUT GETTERS HERE

        elif groceries_choice == 4:
            say_goodbye()
            quit_program = True

    elif main_menu_choice == 1:
        budget_menu()
        budget_choice = int(input("Please enter choice with corresponding number:"))
        if budget_choice == 1:
            print("Type 'exit' anytime you want to exit the program")
            budget_input = input("Please enter your budget:")
            if budget_input.replace(".", "").isnumeric():
                budget_numeric = float(budget_input)
                total_budget = budget_numeric
                print(f"Budget is at ($): {total_budget:.2f}")

        elif budget_choice == 2:
            say_goodbye()
            quit_program = True

    else:
        print("Invalid response.")

       
