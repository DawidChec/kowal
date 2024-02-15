import random
from functions import item

item_name = input("Enter your item name: ")
level_item = int(input("Type in item lvl: "))

while True:
    user_upgrades = input("Uppgrade your item? (+/-): ")
    if user_upgrades == "+":
        if level_item <= 11:
            level_item = item(level_item) + random.randint(1, 3)
            print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")

        elif level_item == 12:
            chance = random.randint(1, 100)
            if chance <= 40:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 1)
                print(f"{item_name} has burned to + {level_item}")

        elif level_item == 13:
            chance = random.randint(1, 100)
            if chance <= 50:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 14:
            chance = random.randint(1, 100)
            if chance <= 30:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 15:
            chance = random.randint(1, 100)
            if chance <= 24:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 16:
            chance = random.randint(1, 100)
            if chance <= 10:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 17:
            chance = random.randint(1, 100)
            if chance <= 14:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 18:
            chance = random.randint(1, 100)
            if chance <= 8:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 19:
            chance = random.randint(1, 100)
            if chance <= 2:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 20:
            chance = random.randint(1, 100)
            if chance <= 1:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 21:
            chance = random.randint(1, 100)
            if chance <= 3:
                level_item = item(level_item) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 22:
            chance = random.randint(1, 100)
            if chance <= 3:
                level_item = item(level_item) + random.randint(1, 2)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)
                print(f"{item_name} has burned to +{level_item}")

        elif level_item == 23:
            chance = random.randint(1, 100)
            if chance <= 4:
                level_item = item(level_item) + random.randint(1, 1)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                level_item = item(level_item) - random.randint(0, 2)

                print(f"{item_name} has burned to +{level_item}")

    elif user_upgrades == "-":
        level_item = level_item - 1
        print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")


    continue_upgrades = input("Do you wish to still upgrade? (Y/n): ").lower()
    if continue_upgrades != "y":
        break

print("Thank you for upgrading.")