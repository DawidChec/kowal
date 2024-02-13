import random

def item(x):
    return x

item_name = input("Enter your item name: ")
level_item = int(input("Type in item lvl: "))

while True:
    user_upgrades = input("Uppgrade your item? (+/-): ")
    if user_upgrades == "+":
        if level_item <= 11:
            upgraded_item = item(level_item) + random.randint(1, 3)
            level_item = upgraded_item
            print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")

        elif level_item == 12:
            chance = random.randint(1, 100)
            if chance <= 40:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 1)
                level_item = burned_item
                print(f"{item_name} has burned to + {burned_item}")

        elif level_item == 13:
            chance = random.randint(1, 100)
            if chance <= 50:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 14:
            chance = random.randint(1, 100)
            if chance <= 30:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 15:
            chance = random.randint(1, 100)
            if chance <= 24:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 16:
            chance = random.randint(1, 100)
            if chance <= 10:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 17:
            chance = random.randint(1, 100)
            if chance <= 14:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 18:
            chance = random.randint(1, 100)
            if chance <= 8:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 19:
            chance = random.randint(1, 100)
            if chance <= 2:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 20:
            chance = random.randint(1, 100)
            if chance <= 1:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 21:
            chance = random.randint(1, 100)
            if chance <= 3:
                upgraded_item = item(level_item) + random.randint(1, 3)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 22:
            chance = random.randint(1, 100)
            if chance <= 3:
                upgraded_item = item(level_item) + random.randint(1, 2)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")

        elif level_item == 23:
            chance = random.randint(1, 100)
            if chance <= 4:
                upgraded_item = item(level_item) + random.randint(1, 1)
                level_item = upgraded_item
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                burned_item = item(level_item) - random.randint(0, 2)
                level_item = burned_item
                print(f"{item_name} has burned to +{burned_item}")



    continue_upgrades = input("Do you wish to still upgrade? (Y/n): ").lower()
    if continue_upgrades != "y":
        break
