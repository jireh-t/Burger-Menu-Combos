"""Version 2 of add combo, trialling a different way to ask the user for
their combo. Uses multiple enter boxes rather than a combined multenterbox """

import easygui

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

combo_name = easygui.enterbox("Enter combo name", "Combo name")
burger = easygui.enterbox("Enter burger name", "Burger")
side = easygui.enterbox("Enter side name", "Side")
drink = easygui.enterbox("Enter drink name", "Drink")

# Get prices of combos
burger_price = easygui.enterbox(f"Enter the price of {burger}", "Burger price")
side_price = easygui.enterbox(f"Enter the price of {side}", "Side price")
drink_price = easygui.enterbox(f"Enter the price of {drink}", "Drink price")

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

