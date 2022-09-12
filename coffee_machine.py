MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 60,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
machine_on = True

#Print report.
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    
#Check resources sufficient?
def check_resources(user_input):
    stocked = True
    if MENU[user_input]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
        stocked = False
    if MENU[user_input]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
        stocked = False
    if MENU[user_input]['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk.")
        stocked = False
    if stocked == False:
        return False
    else: return True

#Takes money and refunds if not enough.
def process_coins():
    user_payment = 0
    print("Please insert coins.")
    q = int(input("Input number of Quarters?: "))
    d = int(input("Input number of dimes?: "))
    n = int(input("Input number of nickels?: "))
    p = int(input("Input numbeer of pennies?: "))
    user_payment = ((q*.25)+(d*.10)+(n*.05)+(p*.01))
    user_change = user_payment - MENU[user_input]['cost']
    if user_payment < MENU[user_input]['cost']:
        print("Sorry that is not enough money. Money refunded")
        return False
    else:
        print(f"Here is ${user_change:.2f} dollars in change")
        resources["money"] += (user_payment - user_change)
        return True
        

#Make coffee by reducing the resources by the recipe amount.
def make_coffee():
   resources['water'] = resources['water'] - (MENU[user_input]['ingredients']['water'])
   resources['milk'] = resources['milk'] - (MENU[user_input]['ingredients']['milk'])
   resources['coffee'] = resources['coffee'] - (MENU[user_input]['ingredients']['coffee'])
   print("Enjoy your coffee!")

#Loop to continue making coffee until 'off' command is given.
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "report":
        print_report()
    if user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        if check_resources(user_input) == True:
            if process_coins() == True:
                make_coffee()
    if user_input == "off":
        machine_on = False


