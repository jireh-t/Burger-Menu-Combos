"""Builds on the code from version 1, adds a confirmation statement and
blank checker"""

import easygui


# Function to make sure input is entered and not left blank
def blank_checker(question, title):
    error_message = "You must fill out every field"

    # Asks user for input
    answer = easygui.enterbox(question, title)

    while True:  # Loops until valid input is entered
        if answer == "":  # Checks if it is blank
            easygui.msgbox(error_message, "ERROR")  # Display error message
            answer = easygui.enterbox(question, title)
        else:
            return answer


# Main Routine

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

combo = ""
for combo_name, combo_info in combos.items():
    name = f"{combo_name}"

    for key in combo_info:
        combo += f"{key}: {combo_info[key]}\n"


menu = ""

# Loop to print full menu
for combo_name, combo_info in combos.items():

    # Print the combo name
    menu += f"\n{combo_name}\n"

    # Print the combo items and price
    for key, value in combo_info.items():
        menu += f"{key}: {value} \n"

# Output the full menu and ask the user what combo to delete
choice = blank_checker(f"/ / / Below is the full menu of combos/ / /\n\n"
                          f"{menu}\n\n"
                          "Which combo would you like to delete?").upper()

# Show error message if the combo is not in the menu

while choice not in combos:
    easygui.msgbox(f"Sorry, {choice} is not in the menu", "ERROR")

    # Output the full menu and ask the user what combo to delete
    choice = blank_checker(f"/ / / Below is the full menu of combos/ / /\n\n"
                           f"{menu}\n\n"
                           "Which combo would you like to delete?",
                           "ENTER COMBO NAME").upper()

sure = easygui.buttonbox(f"Are you sure you want to delete {choice} from the "
                         f"menu?\n\n"
                         f"This cannot be undone",
                         "PLEASE CONFIRM",
                         choices=["Yes", "No"])

if sure == "Yes":
    # Delete the combo
    del[combos[choice]]
    easygui.msgbox(f"{choice} has been deleted", "DELETED")

