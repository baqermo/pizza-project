def order_pizza(order):
    """
    Allows the user to select pizza size, toppings with quantity,
    and number of pizzas and. Updates the order dictionary.
    """
    # Reset order
    order.clear()
    order['size'] = ''
    order['toppings'] = {}  # {for topping kind and amount}
    order['amount'] = 0
    order['total'] = 0.0

    # Pizza sizes and prices to calculate
    sizes = {'S': 5.99, 'M': 7.99, 'L': 9.99}
    print("Small = 5.99\nMedium = 7.99\nLarge = 9.99")
    
    # Select size
    while True:
        size = input("What size would you like? (Type S, M, or L): ").upper()
        if size in sizes:
            order['size'] = size
            break
        else:
            print("Please input a valid size (S, M, or L).")
    
    # Toppings list and prices
    topping_options = {
        '1': ('Pepperoni', 1.99),
        '2': ('Sausage', 1.99),
        '3': ('Ham', 1.99),
        '4': ('Bell Peppers', 1.99),
        '5': ('Bacon', 2.99),
        '6': ('Olives', 2.99),
        '7': ('Anchovy', 2.99)
    }
    # Select toppings
    print("Now add toppings! Every pizza already has sauce and cheese included.")
    for num, (name, price) in topping_options.items():
        print(f"{num}. {name} = {price}")
    # Topping selection loop
    while True:
        choice = input("Choose a topping by number (or type X to finish): ").upper()
        if choice == 'X':
            break
        elif choice in topping_options:
            topping_name, topping_price = topping_options[choice]
            # Check if topping already added and prompt topping option again to add something else
            if topping_name in order['toppings']:
                print(f"{topping_name} is already on the pizza.")
                continue
            
            # Ask for quantity of topping (light, normal, extra)
            while True:
                print("1. Light 2. Normal 3. Extra")
                amount_choice = input(f"Select amount for {topping_name} (1-3): ")
                if amount_choice in ['1', '2', '3']:
                    amount_map = {'1': 'Light', '2': 'Normal', '3': 'Extra'}
                    order['toppings'][topping_name] = amount_map[amount_choice]
                    print(f"{topping_name} ({amount_map[amount_choice]}) added!")
                    break
                else:
                    print("Please choose 1, 2, or 3 for amount.")

            # Ask if user wants more toppings
            more = input("Do you want to add more toppings? (Yes or No): ").lower()
            if more == 'no':
                break
        else:
            print("Invalid choice. Enter 1-7 or X to finish.")

    #ask how many pizzas they want to order and make sure its a valid number entry more than 0
    while True:
        try:
            amount = int(input("How many pizza's you would like to order? "))
            if amount > 0:
                order['amount'] = amount
                break
            else:
                print("Amount must be at least 1.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("Order saved! You can view your cart or checkout when ready.")

def view_cart(order):
    """
    Displays the current order including number of pizzas, toppings with amounts, and total price.
    """
    #if they have no order, cart and checkout cannot be be opened, prompting them to order first
    if not order or order['size'] == '':
        print("Please place an order first!")
        return

    # Prices for toppings to calculate
    size_prices = {'S': 5.99, 'M': 7.99, 'L': 9.99}
    topping_prices = {
        'Pepperoni': 1.99, 'Sausage': 1.99, 'Ham': 1.99,
        'Bell Peppers': 1.99, 'Bacon': 2.99, 'Olives': 2.99,
        'Anchovy': 2.99
    }

    # Calculate total price by adding toppings, number of pizza, and size
    total = size_prices[order['size']]
    for topping in order['toppings']:
        total += topping_prices[topping]
    total *= order['amount']
    order['total'] = total
    #convert single letter entry into a string and get stored
    size_names = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}
    print(f"{order['amount']} {size_names[order['size']]} Pizza(s)")
    #takes the added topping added and convert into string to tell user what they have added
    if order['toppings']:
        toppings_str = ', '.join([f"{name} ({amt})" for name, amt in order['toppings'].items()])
    else:
        toppings_str = "Cheese Only"
    print("Toppings added:", toppings_str)
    print("Your total is:", total)
    print("Please proceed to checkout if you would like to confirm this order!")

def checkout(order):
    """
    Confirms their order and exit the program
    """
    if not order or order['size'] == '':
        print("Please place an order first!")
        return
    view_cart(order)
    while True:
        choice = input(f"Your total is ${order['total']}, Would you like to Checkout? (Yes or No): ").lower()
        if choice == 'yes':
            print("Thanks for shopping with us! Your order should arrive soon.")
            exit()
        elif choice == 'no':
            print("You can view your cart again or add more toppings.")
            break
        else:
            print("Please type Yes or No.")

def main_menu():
    """
    Main menu loop to order, view cart, checkout, or exit.
    """
    order = {}
    while True:
        print("PIZZA ORDERING MENU")
        print("1. Order Pizza")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose an option 1-4: ")
        if choice == '1':
            order_pizza(order)
        elif choice == '2':
            view_cart(order)
        elif choice == '3':
            checkout(order)
        elif choice == '4':
            print("Goodbye, have a great day!")
            break
        else:
            print("Please pick a choice from 1 to 4.")
# call main function to start the program
main_menu()