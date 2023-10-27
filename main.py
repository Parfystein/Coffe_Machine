from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def get_ingredients(ORDER):
    ingredients = ORDER["ingredients"]
    return ingredients

def refill_machine():
    add_water = int(input("How much water would you like to add? "))
    add_milk = int(input("How much milk would you like to add? "))
    add_coffee = int(input("How much coffee would you like to add? "))
    resources["water"]+=add_water
    resources["milk"]+=add_milk
    resources["coffee"]+=add_coffee
    return "Thank you! The machine has been refilled!"

def withdraw_money():
    initial_money = resources["money"]
    print(f"${initial_money} dollars have been withdrawn.")
    resources["money"] = 0
def check_water(ORDER):
    ingredients = get_ingredients(ORDER)
    water_required = ingredients["water"]
    if resources["water"] > water_required:
        return 1
    else:
        print("Sorry, there is not enough water.")
        return 0

def check_milk(ORDER):
    ingredients = get_ingredients(ORDER)
    milk_required = ingredients["milk"]
    if resources["milk"] > milk_required:
        return 1
    else:
        print("Sorry, there is not enough milk.")
        return 0

def check_coffee(ORDER):
    ingredients = get_ingredients(ORDER)
    coffee_required = ingredients["coffee"]
    if resources["coffee"] > coffee_required:
        return 1
    else:
        print("Sorry, there is not enough coffee.")
        return 0

def subtract_water(ORDER):
    ingredients = get_ingredients(ORDER)
    water_required = ingredients["water"]
    resources["water"] = resources["water"] - water_required

def subtract_coffee(ORDER):
    ingredients = get_ingredients(ORDER)
    coffee_required = ingredients["coffee"]
    resources["coffee"] = resources["coffee"] - coffee_required

def subtract_milk(ORDER):
    ingredients = get_ingredients(ORDER)
    milk_required = ingredients["milk"]
    resources["milk"] = resources["milk"] - milk_required

def money_transaction(ORDER, user_order):
    cost = ORDER["cost"]
    print(f"The drink will cost you {cost}$.")
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickels = int(input("Insert nickels: "))
    pennies = int(input("Insert pennies: "))
    sum = round((0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies),2)
    if sum == cost:
        resources["money"]+=sum
    elif sum > cost:
        resources["money"]= round((resources["money"] + sum),2)
        change = round((sum - cost),2)
        resources["money"] = round((resources["money"] - change),2)
        print(f"Thank you! Your change is ${change} dollars.\nHere is your {user_order}!")
        return True
    else:
        print("Sorry, that's not enough money! Money refounded.")
        return 0
def report():
    print (f"Water: {resources['water']}ml")
    print (f"Milk: {resources['milk']}ml")
    print (f"Coffee: {resources['coffee']}g")
    print (f"Money: ${resources['money']}")

def is_in_drinks(order):
    order_present=0
    for key in MENU:
        if order==key:
            order_present+=1
    return order_present

def machine():
    user_order = (input("What drink would you like to order? Latte/Cappuccino/Espresso: ")).lower()
    if is_in_drinks(user_order)==1:
        ORDER = MENU[user_order]
        get_ingredients(ORDER)
        if user_order == "espresso":
            checker =check_coffee(ORDER) + check_water(ORDER)
            if checker == 2:
                if money_transaction(ORDER, user_order) == True:
                    subtract_water(ORDER)
                    subtract_coffee(ORDER)
                    return 1
                else:
                    return 1
            else:
                print("Sorry! Not all ingredients are available for your drink!")
                return 1
        else:
            checker = check_milk(ORDER)+check_coffee(ORDER)+check_water(ORDER)
            if checker == 3:
                if money_transaction(ORDER, user_order) == True:
                    subtract_milk(ORDER)
                    subtract_water(ORDER)
                    subtract_coffee(ORDER)
                    return 1
                else:
                    return 1
            else:
                print("Sorry! Not all ingredients are available for your drink!")
                return 1
    elif user_order == "off":
        print("Have a good day!")
        exit()
    elif user_order=="report":
        report()
        return 1
    elif user_order == "refill":
        refill_machine()
        return 1
    elif user_order == "withdraw":
        withdraw_money()
        return 1
    else:
        print("The drink you order is not in the menu or invalid name!")
        return 1

while machine() == 1:
    machine()