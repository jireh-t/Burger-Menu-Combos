"""Burger Menu Combos base component
Components added after they have been created and tested"""

import easygui


# Function to display welcome screen and menu
def welcome():
    easygui.msgbox("Welcome to Burger Menu Combos")
    choice = easygui.buttonbox("What would you like to do?\n", "Options",
                               choices=["1) Add combo", "2) Search combo",
                                        "3) Delete combo", "4) Output combo",
                                        "5) Exit"])
    return choice


# Main Routine
option = welcome()

if option == "1) Add combo":
    print("Add combo")

elif option == "2) Search combo":
    print("Search combo")

elif option == "3) Delete combo":
    print("Delete combo")

elif option == "4) Output combo":
    print("Output combo")

elif option == "5) Exit":
    print("Goodbye")




