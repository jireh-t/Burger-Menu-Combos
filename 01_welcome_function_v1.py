"""Welcome/ Menu Function
based on 01_welcome_v3
"""

import easygui


def welcome():
        easygui.msgbox("Welcome to Burger Menu Combos")
        choice = easygui.buttonbox("What would you like to do?\n", "Options",
                                   choices=["1) Add combo", "2) Search combo",
                                            "3) Delete combo", "4) Output combo",
                                            "5) Exit"])
        return choice


# Main Routine
option = welcome()
print(f"You entered '{option}'")

