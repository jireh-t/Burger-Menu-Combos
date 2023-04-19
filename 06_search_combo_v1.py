"""Version 1 of component 6 search combo"""

import easygui

# Stores burger combos in a nested dictionary
combos = {"VALUE":
            {"Beef Burger": "$5.69",
             "Fries": "$1.00",
             "Fizzy Drink": "$1.00"},
          "CHEEZY":
            {"Cheeseburger": "$6.69",
             "Fries": "$1.00",
             "Fizzy Drink": "$1.00"},
          "SUPER":
            {"Cheeseburger": "$6.69",
             "Large Fries": "$2.00",
             "Smoothie": "$2.00"}
          }

# Ask user to enter combo name they want to search
search_name = easygui.enterbox("Enter name of combo", "SEARCH").upper()

if search_name in combos:
    easygui.msgbox(f"{search_name} is in the menu")

else:
    easygui.msgbox(f"Sorry, {search_name} is not in the menu")


