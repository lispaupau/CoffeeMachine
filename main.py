def subtract_ingredients(total, item):
    for ingredient, amount in item['ingredients'].items():
        if ingredient in total:
            if total[ingredient] >= amount:
                total[ingredient] -= amount
            else:
                return False
    return True


def total_money(quarters, dimes, nickles, pennies):
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    round_money = round(money, 2)
    return round_money


def money_count(user, menu, total_ingredients, total_coins):
    if menu[user]['cost'] <= total_coins:
        money_change = total_coins - menu[user]['cost']
        total_ingredients['money'] += menu[user]['cost']
        print(f'Here is ${money_change} in change.')
        print(f'Here is your {user}. Enjoy!')
    else:
        print('Sorry that`s not enough money.')


def coffee_machine():
    total_ingredients = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0,
    }
    while True:
        menu = {
            'espresso': {
                'ingredients': {
                    'water': 50,
                    'coffee': 18,
                },
                'cost': 1.5,
            },
            'latte': {
                'ingredients': {
                    'water': 200,
                    'milk': 150,
                    'coffee': 24,
                },
                'cost': 2.5,
            },
            'cappuccino': {
                'ingredients': {
                    'water': 250,
                    'milk': 100,
                    'coffee': 24,
                },
                'cost': 3.0,
            }
        }
        user = input('What would you like? (espresso/latte/cappuccino): ')
        if user == 'off':
            break
        if user == 'report':
            print(f'Water: {total_ingredients["water"]}ml\nMilk: {total_ingredients["milk"]}ml\n'
                  f'Coffee: {total_ingredients["coffee"]}g\nMoney: ${total_ingredients["money"]}')

        if user in menu:
            if subtract_ingredients(total_ingredients, menu[user]):
                print('Please insert coins.')
                while True:
                    try:
                        quarters = int(input('How many quarters?: '))
                        dimes = int(input('How many dimes?: '))
                        nickles = int(input('How many nickles?: '))
                        pennies = int(input('How many pennies?: '))

                        if quarters < 0 or dimes < 0 or nickles < 0 or pennies < 0:
                            print('Please enter a non-negative quantity of coins')
                            continue
                        money_count(user, menu, total_ingredients, total_money(quarters, dimes, nickles, pennies))
                        break
                    except ValueError:
                        print('Invalid input. Please enter quantity')
            else:
                print(f'Sorry, not enough ingredients for {user}')
        elif user not in menu and user != 'off' and user != 'report':
            print('Invalid input. Please choose from the menu.')


coffee_machine()
