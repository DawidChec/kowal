import random

def item(x):
    return x

level_item = int(input("Type in item lvl. "))

while True:
    user_upgrades = input("Uppgrade your item? (+/-) ")
    if user_upgrades == "+":
        upgraded_item = item(level_item) + random.randint(1, 3)
        level_item = upgraded_item
        print(upgraded_item)

    user_still_upgrades = input("Do you wish to still upgrade? (Y/n): ").lower()
    if user_still_upgrades != "y":
        break
