"""Burger Welcome/ Menu
Puts the code created in v2 into a loop to make testing easier and more
efficient.
"""

import easygui

while True:  # Loop for testing
    easygui.msgbox("Welcome to Burger Menu Combos")
    choice = easygui.buttonbox("What would you like to do?\n", "Options",
                               choices=["1) Add combo", "2) Search combo",
                                        "3) Delete combo", "4) Output combo",
                                        "5) Exit"])

    # Testing the code to make sure it corresponds to the correct option
    if choice == "1) Add combo":
        print("Add combo")

    elif choice == "2) Search combo":
        print("Search combo")

    elif choice == "3) Delete combo":
        print("Delete combo")

    elif choice == "4) Output combo":
        print("Output combo")

    elif choice == "5) Exit":
        print("Goodbye")
        break
