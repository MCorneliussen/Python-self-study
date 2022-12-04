from drinks import MENU, resources

profit = 0


def inserted_coin():
    '''This function stores all the coins inserted in the machine and returns the total.'''
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def have_resources(order_ingredients):
    '''Function that uses a for loop to loop through and see if there are sufficient ingredients.'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True


def transaction_check(money_recieved, drink_cost):
    '''Function to check and verify that there are enough coins in the machine, if true then gives back the change. If not enough then refunds it.'''
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if have_resources(drink["ingredients"]):
            payment = inserted_coin()
            if transaction_check(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        

