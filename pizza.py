# Displays the options 1-4 when program is executed, each with their own function.
def order_pizza():
    # setting variables to check if small, medium, or large is selected
    Small = False
    Medium = False
    Large = False
    SExit = False
    # Displaying prices of pizza
    print("Small = 5.99")
    print("Medium = 7.99")
    print("Large = 9.99")
    # Loop for selecting the pizza size
    while SExit == False:
        size = input("What size would you like? (Type S, M, or L): ")
        if size == 'S':
            Small = True
            SExit = True
        elif size == 'M':
            Medium = True
            SExit = True
        elif size == 'L':
            Large = True
            SExit = True
        elif Small == True or Medium == True or Large == True:
            SExit = True
        else:
            print("Please input a valid size")
    # Displays prices for toppings
    print("Now add toppings! every pizza already has sauce and cheese included")
    print("1. Pepperoni = 1.99")
    print("2. Sausage = 1.99")
    print("3. Ham = 1.99")
    print("4. Bell Peppers = 1.99")
    print("5. Bacon = 2.99")
    print("6. Olives = 2.99")
    print("7. Anchovy = 2.99")
    # Setting variables to check which toppings are added
    TExit = False
    Pepperoni = False
    Olives = False
    Sausage = False
    Anchovy = False
    BellPepper = False
    Ham = False
    Bacon = False
    # Loop for adding toppings
    while TExit == False:
        toppings = input("What toppings would you like to add? (Type X to finish): ")
        if toppings == '1':
            Pepperoni = True
            TExit = True
        elif toppings == '2':
            Sausage = True
            TExit = True
        elif toppings == '3':
            Ham = True
            TExit = True
        elif toppings == '4':
            BellPeppers = True
            TExit = True
        elif toppings == '5':
            Bacon = True
            Exit = True
        elif toppings == '6':
            Olives = True
            TExit = True
        elif toppings == '7':
            Anchovy = True
            TExit = True
        elif toppings == 'X':
            TExit = True
        else:
            print("Please input a valid topping or exit")
    # Amount of pizzas
    Amount = input("Please select the amount of pizza's you would like!: ")
    # Concluding the order and allowing the option to go to a different area
    print("Please select the cart to see your order with the price, or checkout when you feel read!")
    OrderPlaced = True

def view_cart():
    #Setting up price variables for all of the options
    SmallPrice = 5.99
    MediumPrice = 7.99
    LargePrice = 9.99
    PepperoniPrice = 1.99
    SausagePrice = 1.99
    HamPrice = 1.99
    BellPeppersPrice = 1.99
    BaconPrice = 2.99
    OlivesPrice = 2.99
    AnchovyPrice = 2.99
    Total = 0.00
    # Checking for pizza size and adding to total
    if Small == True: 
        print("Small = 5.99")
        Total += SmallPrice
    elif Medium == True: 
        print("Medium = 7.99")
        Total += MediumPrice
    elif Large == True:
        print("Large = 9.99")
        Total += LargePrice
    else:
        print("Please place an order first!")
        main_menu()
    #checking for toppings and adding to total
    if Pepperoni == True:
        print("+ 1.99 (Pepperoni)")
        Total += PepperoniPrice
    elif Olives == True:
        print("+ 2.99 (Olives)")
        Total += OlivesPrice
    elif Sausage == True:
        print("+ 1.99 (Sausage)")
        Total += SausagePrice
    elif Anchovy == True:
        print("+ 2.99 (Anchovy)")
        Total += AnchovyPrice
    elif BellPeppers == True:
        print("+ 1.99 (BellPepper)")
        Total += BellPeppersPrice
    elif Ham == True:
        print("+ 1.99 (Ham)")
        Total += HamPrice
    elif Bacon == True:
        print("+ 2.99 (Bacon)")
        Total += BaconPrice
    # Multiplying by amount of pizza's
    Total = Total * Amount
    print(Amount, " Pizza's")
    print("Your total is:", Total)
    print("Please proceed to checkout if you would like to confirm this order!")

def checkout():
    CheckingOut = input("Your total is $", Total, ", Would you like to Checkout? (Yes or No): ")
    if input == 'Yes':
        print("Thanks for shopping with us! Your order should arrive soon")
    elif input == 'No':
        print("If you would like to check your order again, View your cart")


def main_menu():
    Mexit = False
    while Mexit == False:
        print("PIZZA ORDERING MENU")
        print("1. Order Pizza")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")
        """
        Displays the menu with number choices to pick from, user must pick numbers 1-4
        or they will get a message prompting them to pick from the options. based on the number
        they pick, they will get the menu of pizzas, checkout, see their cart, or exit the menu.
        """
        choice = 0
        choice = input("Choose an option 1-4: ")
        if choice =="1":
            order_pizza()
        elif choice =="2":
            if OrderPlaced == True:
                view_cart()
            else:
                print("Please place an order first!")
        elif choice =="3":
            if OrderPlaced == True:
                checkout()
            else:
                print("Please place an order first!")
        elif choice =="4":
            print("Goodbye, Have a great day!")
            Mexit = True
        else:
            print("Please pick a Choice from 1 to 4")
OrderPlaced = False
main_menu()
