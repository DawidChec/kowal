import random
from functions import item

item_name = input("Enter your item name: ")
item_level = int(input("Type in item lvl: "))

while True:
    user_upgrades = input("Uppgrade your item? (+/-): ")
    if user_upgrades == "+":
        if item_level <= 11:
            item_level = item(item_level) + random.randint(1, 3)
            print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")

        elif item_level == 12:
            chance = random.randint(1, 100)
            if chance <= 40:
                level_item = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                level_item = item(item_level) - random.randint(0, 1)
                print(f"{item_name} has burned to + {item_level}")

        elif item_level == 13:
            chance = random.randint(1, 100)
            if chance <= 50:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 14:
            chance = random.randint(1, 100)
            if chance <= 30:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{level_item}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 15:
            chance = random.randint(1, 100)
            if chance <= 24:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 16:
            chance = random.randint(1, 100)
            if chance <= 10:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 17:
            chance = random.randint(1, 100)
            if chance <= 14:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 18:
            chance = random.randint(1, 100)
            if chance <= 8:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 19:
            chance = random.randint(1, 100)
            if chance <= 2:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 20:
            chance = random.randint(1, 100)
            if chance <= 1:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 21:
            chance = random.randint(1, 100)
            if chance <= 3:
                item_level = item(item_level) + random.randint(1, 3)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 22:
            chance = random.randint(1, 100)
            if chance <= 3:
                item_level = item(item_level) + random.randint(1, 2)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)
                print(f"{item_name} has burned to +{item_level}")

        elif item_level == 23:
            chance = random.randint(1, 100)
            if chance <= 4:
                item_level = item(item_level) + random.randint(1, 1)
                print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")
            else:
                item_level = item(item_level) - random.randint(0, 2)

                print(f"{item_name} has burned to +{item_level}")

    elif user_upgrades == "-":
        item_level += - 1
        print(f"Congratulations! Your item {item_name} has been uppgraded to +{item_level}.")


    continue_upgrades = input("Do you wish to still upgrade? (Y/n): ").lower()
    if continue_upgrades != "y":
        break

print("Thank you for upgrading.")