import random

def item(x):
    return x

level_item = int(input("Type in item lvl: "))

while True:
    user_upgrades = input("Uppgrade your item? (+/-): ")
    if user_upgrades == "+":
        if level_item <= 11:
            upgraded_item = item(level_item) + random.randint(1, 3)
            level_item = upgraded_item
            print(upgraded_item)

        elif level_item == 12:
            chance = random.randint(1, 100)
            if chance <= 1:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(upgraded_item)
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(burned_item)




    continue_upgrades = input("Do you wish to still upgrade? (Y/n): ").lower()
    if continue_upgrades != "y":
        break
