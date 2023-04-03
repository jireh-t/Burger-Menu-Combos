"""This code will be trial 1 of storing, adding, and printing the existing
burger combos in different storage units"""

import easygui

# Stores burger combos in a 2 dimensional dictionary
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

text = "Enter the following combo items"  # Prompt for user to type
title = "Enter combo"  # Title shown
input_list = ["Combo name", "Burger", "Side", "Drink"]  # Fields to fill in

# User's inputs are added to a list
enter = easygui.multenterbox(text, title, input_list)




