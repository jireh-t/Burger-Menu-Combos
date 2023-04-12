"""Welcome/ Menu Function
based on 01_welcome_v3, later after I have developed the other functions I
will replace the print statements with function calls
"""

import easygui


def welcome():
    easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")
    # Allow the user to select what they want to do
    choice = easygui.buttonbox("What would you like to do?\n", "Options",
                               choices=["1) Add combo", "2) Search combo",
                                        "3) Delete combo", "4) Output combo",
                                        "5) Exit"])
    return choice


# Main Routine
option = welcome()

# Will call on corresponding functions
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



