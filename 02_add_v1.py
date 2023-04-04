"""This code will be trial 1 of storing, adding, and printing the existing
burger combos in different storage units"""

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
input_price = [f"{items[1].upper()}", f"{items[2]}", f"{items[3]}"]
# Prices added to a list
prices = easygui.multenterbox(price_text, price_title, input_price)

# Add the user's combo to the existing combos


easygui.msgbox(f"Is the following combo correct?\n\n"
               f"{items[0].upper()}\n"
               f"{items[1]}: ${prices[0]}\n"
               f"{items[2]}: ${prices[1]}\n"
               f"{items[3]}: ${prices[2]}\n")
