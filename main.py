menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee":18
        },
        "cost" : 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffee":150,
            "milk": 24
        },
        "cost" : 2.5,
    },

    "cappuccino":{
        "ingredients":{
            "water": 250,
            "coffee":100,
            "milk":24,
        },
        "cost" : 3.0,
    }
}
profit = 0 
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 300,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def prosses_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.01
    total += int(input("how many pennies?: ")) * 0.05
    return total
def is_transaction_successfull(money_recived, drink_cost):
    if money_recived > drink_cost:
        change = round(money_recived - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refounded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}")
       print(f"Milk: {resources['milk']}")
       print(f"Coffee: {resources['coffee']}")
       print(f"Money: {profit }")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
             payment = prosses_coins()
             if is_transaction_successfull(payment, drink["cost"]):
                 make_coffee(choice, drink["ingredients"])