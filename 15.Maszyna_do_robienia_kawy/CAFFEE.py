MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_res(w,m,c):
    if resources["water"] < w:
        print("not enough water")
        return False
    elif resources["milk"] < m:
        print("not enough milk")
        return False
    elif resources["coffee"] < c:
        print("not enough coffee")
        return False
    else:
        return True

def calculate(q,d,n,p):
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01
    total = quarter * q + dime * d + nickle * n + penny * p
    return total


while True:
    coffee = input("What would you like? (espresso / latte /cappuccino): ")
    if coffee == "off":
        break
    elif coffee == "report":
        print(resources)
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        a = MENU[coffee]
        cost = a['cost']
        ingredients = a['ingredients']
        water = ingredients["water"]
        milk = ingredients["milk"]
        coffee_i = ingredients["coffee"]
        check_res(water,milk,coffee_i)

        print("Please insert coins")
        quarters = int(input("Quarters ($0.25): "))
        dimes = int(input("Dimes ($0.10): "))
        nickles = int(input("Nickles ($0.05): "))
        pennies = int(input("Pennies ($0.01): "))
        total = calculate(quarters,dimes,nickles,pennies)

        if total < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print("Coffee cost: {0} \nYou gave: {1} \nYour change: {2}".format(cost, round(total,2),round(total - cost,2)))
            resources["water"] = resources["water"] - water
            resources["milk"] = resources["milk"] - milk
            resources["coffee"] = resources["coffee"] - coffee_i
            resources["money"] = resources["money"] + cost
            print("Here is your {}, enjoy!".format(coffee))
            print(resources)




        

    
