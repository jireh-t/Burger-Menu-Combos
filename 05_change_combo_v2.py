"""Trial 2 of change combo component, if the combo is incorrect the entering
process restarts"""

import easygui


# Float checking function - loops until a valid number is entered
def float_checker(question, low, high, item):
    error = "That was not a valid input\n" \
            "Please enter a price above ${} and below ${}\n".format(low, high)

    # Keep asking until a valid amount (0-40) is entered
    while True:
        try:
            # Ask for price
            number = float(easygui.enterbox(question, item))

            # Check for number within the required range
            if low < number <= high:
                number = f"${number:.2f}"
                return number
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error, "Error")


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
while True:
    new_combo = {}

    # Get items in combos
    combo_name = blank_checker("Enter combo name", "COMBO NAME").upper()
    burger = blank_checker("Enter burger name", "BURGER").title()
    side = blank_checker("Enter side name", "SIDE").title()
    drink = blank_checker("Enter drink name", "DRINK").title()

    # Get prices of combos
    burger_price = float_checker(f"Enter the price of {burger}", 0, 40, "BURGER")
    side_price = float_checker(f"Enter the price of {side}", 0, 25, "SIDE")
    drink_price = float_checker(f"Enter the price of {drink}", 0, 15, "DRINK")

    # Add the user's combo to a new dictionary

    new_combo[combo_name] = {}  # Adds key of combo name and empty dictionary
    new_combo[combo_name][burger] = burger_price  # Adds burger and price
    new_combo[combo_name][side] = side_price  # Adds side and price
    new_combo[combo_name][drink] = drink_price  # Adds drink and price

    # Print the combo and check with user that it is correct
    combo = ""
    for combo_name, combo_info in new_combo.items():
        name = f"{combo_name}"

        for food in combo_info:
            combo += f"{food}: {combo_info[food]}\n"

    choice = easygui.buttonbox(f"/ / / Is the following combo correct? / / "
                               f"\n\n"
                               f"{name}\n\n"
                               f"{combo}",
                               "PLEASE CONFIRM",
                               choices=["Yes", "No"])
    if choice == "Yes":
        break

    else:
        easygui.msgbox("Sorry, please try again")

