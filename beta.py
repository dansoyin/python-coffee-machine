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
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 300,
}

amount = 0


def coint():
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = (
    pennies * 0.01 +
    nickles * 0.05 +
    dimes * 0.10 +
    quarters * 0.25
    )
    return total

def coffee_machine(gueses):
    global amount
    for item in menu[gueses]["ingredients"]:
        if resources[item] < menu[gueses]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return

    money = coint()

    if money >= menu[gueses]["cost"]:
        amount += menu[gueses]["cost"]
        change = money - menu[gueses]["cost"]

        resources["coffee"] -= menu[gueses]["ingredients"]["coffee"]
        resources["water"] -= menu[gueses]["ingredients"]["water"]
        if "milk" in menu[gueses]["ingredients"]:
            resources["milk"] -= menu[gueses]["ingredients"]["milk"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {gueses} Enjoy!")

    else:
        print("Your money not enought, we will back your money")
        money = 0

should_be_next = True
while should_be_next:
    guess = input("What would you like? (espresso/latte/cappuccino): ")
    if guess == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {amount}")
    elif guess == "latte":
        coffee_machine("latte")
    elif guess == "cappuccino":
        coffee_machine("cappuccino")
    elif guess == "espresso":
        coffee_machine("espresso")
    elif guess == "off":
        print("see you next time :D")
        should_be_next = False
    else:
        print("Wrong input, pls try again.")

