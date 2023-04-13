"""Puts the float function 03_float_checker_v4_function into the code.
Building on the code from version 2"""

import easygui


# Float checking function - loops until a valid number is entered
def float_checker(question, low, high, item):
    error = "That was not a valid input\n" \
            "Please enter a price above ${} and below ${}\n".format(low, high)

    # Keep asking until a valid amount (0-40) is entered
    while True:
        try:
            # Ask for price
            number = float(easygui.enterbox(question, item))

            # Check for number within the required range
            if low < number <= high:
                number = f"${number:.2f}"
                return number
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error, "Error")


# Stores burger combos in a nested dictionary
combos = {"VALUE":
            {"Beef Burger": 5.69,
             "Fries": 1.00,
             "Fizzy drink": 1.00},
          "CHEEZY":
            {"Cheeseburger": 6.69,
             "Fries": 1.00,
             "Fizzy drink": 1.00},
          "SUPER":
            {"Cheeseburger": 6.69,
             "Large fries": 2.00,
             "Smoothie": 2.00}
          }

new_combo = {}

# Get items in combos

combo_name = easygui.enterbox("Enter combo name", "COMBO NAME")
burger = easygui.enterbox("Enter burger name", "BURGER")
side = easygui.enterbox("Enter side name", "SIDE")
drink = easygui.enterbox("Enter drink name", "DRINK")

# Get prices of combos
burger_price = float_checker(f"Enter the price of {burger}", 0, 40, "BURGER")
side_price = float_checker(f"Enter the price of {side}", 0, 25, "SIDE")
drink_price = float_checker(f"Enter the price of {drink}", 0, 15, "DRINK")

# Add the user's combo to a new dictionary

new_combo[combo_name] = {}  # Adds key of combo name and empty dictionary
new_combo[combo_name][burger] = burger_price # Adds burger and price
new_combo[combo_name][side] = side_price  # Adds side and price
new_combo[combo_name][drink] = drink_price  # Adds drink and price

# Print the combo and check with user that it is correct
combo = ""
for combo_name, combo_info in new_combo.items():
    name = f"{combo_name}"

    for food in combo_info:
        combo += f"{food}: {combo_info[food]}\n"

easygui.buttonbox(f"Is the following combo correct?\n\n"
                  f"{name}\n\n"
                  f"{combo}",
                  choices=["Yes", "No"])
