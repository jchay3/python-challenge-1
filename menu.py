# menu.py
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)
            # Prompt the customer to enter their Selection
            menu_selection = input(f"Please enter the item number you wish to add to your order or 'q' to return to the main menu: ")

            #Quit the menu if the user chooses 'q'
            if menu_selection == 'q':
                continue
            # Validation to check if the input is a valid number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                
            # Check if selection is valid menu item
            if 1 <= menu_selection < item_counter:
                # The selection is valid, process the order
                item_counter = 1
                selected_item = None
                selected_price = 0

                #loop through the menu and find item
                for key, value in menu[menu_category_name].items():
                    if type(value) is dict:
                        #Iterate through dictionary Items
                        for key2, value2 in value.items():
                            if item_counter == menu_selection:
                                selected_item = f"{key} - {key2}"
                                selected_price = value2
                                break
                            item_counter += 1
                    else:
                        if item_counter == menu_selection:
                            selected_item = key
                            selected_price = value
                        item_counter += 1

# Now ask the user for the quantity
if selected_item:
    print(f"You have selected: {selected_item} for ${selected_price}")
    quantity = input(f"How many {selected_item} would you like to order?")

    # Confirm that quantity is a positive number
    if quantity.isdigit() and int(quantity) > 0:
        quantity = int(quantity)  

        # Add selected Item to the order list as a dictionary
        order.append({
            "Item name": selected_item,
            "Price": selected_price,
            "Quantity": quantity
        })

        print(f"Added {quantity} of {selected_item} to your order.")
    else:
        print("Invalid quantity. Please enter a number greater than 0.")
else:
    print("Invalid selection. Please try again.")


                print(f"added {quanity} of {selected_item} to your order.")
                   else:
                    print("Invalid quanity. please enter a number greater than 0.")
                else:
                    print("Invalid selection. Please try again.")
            else:
                print("Invalid item number. Please select a valid item number from the menu.")
          else:
            # if the input isn't a number
            print("Invalid input. Please enter a valid number.")         


                                 


