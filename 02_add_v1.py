"""Component 2 Add combo version 1
This code will be trial 1 using an enterbox with multiple fields to get the
user's combo"""

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

text = "Enter the following combo items"  # Prompt for user to type
title = "Enter combo"  # Title shown
input_list = ["Combo name", "Burger", "Side", "Drink"]  # Fields to fill in
# User's inputs are added to a list
items = easygui.multenterbox(text, title, input_list)

# Get prices of combos

price_text = "Enter the prices of your items"  # Prompt user for prices
price_title = "Enter prices"  # Title shown
# Prices to fill
input_price = [f"{items[1]}", f"{items[2]}", f"{items[3]}"]
# Prices added to a list
prices = easygui.multenterbox(price_text, price_title, input_price)

# Add the user's combo to a new dictionary

new_combo[items[0]] = {}  # Adds key of combo name and empty dictionary
new_combo[items[0]][items[1]] = prices[0]  # Adds burger and price
new_combo[items[0]][items[2]] = prices[1]  # Adds side and price
new_combo[items[0]][items[3]] = prices[2]  # Adds drink and price

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
