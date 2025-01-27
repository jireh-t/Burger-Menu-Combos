"""Version 4 of change combo component. Adding the Float checker and blank
checker functions to the code"""

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
                easygui.msgbox(error, "ERROR")

        except ValueError:
            easygui.msgbox(error, "ERROR")


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

# Combo to change
new_combo = {"SUPER":
            {"Cheeseburger": "$6.69",
             "Large Fries": "$2.00",
             "Smoothie": "$2.00"}}

# Keep looping until the combo is correct
while True:

    # Print the combo and check with user that it is correct
    combo = ""
    for combo_name, combo_info in new_combo.items():
        name = f"{combo_name}"

        for food in combo_info:
            combo += f"{food}: ${combo_info[food]:.2f}\n"

    # Confirm the combo with the user
    choice = easygui.buttonbox(f"/ / / Is the following combo correct? / / "
                               f"/\n\n"
                               f"{name}\n\n"
                               f"{combo}",
                               "PLEASE CONFIRM",
                               choices=["Yes", "No"])
    if choice == "Yes":
        break

    # Ask the user what they would like to change
    change = easygui.buttonbox("What would you like to change?",
                               "Select Below",
                               choices=["Combo name", "Item name",
                                        "Price"])

    if change == "Combo name":

        # Ask user for new combo name
        combo_name_change = blank_checker("What would you like to change it "
                                          "to?", "New Combo Name").upper()

        # Replace the combo name with new name
        new_combo[combo_name_change] = new_combo.pop(combo_name)

    elif change == "Item name":

        # Ask user for current item they wish to change
        item_change = blank_checker("Enter the name of the item you want to "
                                    "change\n\n"
                                    f"{name}\n\n"
                                    f"{combo}", "Current Item").title()

        # Give error message if item does not exist
        while item_change not in new_combo[combo_name]:
            easygui.msgbox(f"Sorry {item_change} is not in the original "
                           f"combo")

            # Keep asking user until valid item is entered
            item_change = blank_checker("Enter the name of the item you want"
                                        " to change\n\n"
                                        f"{name}\n\n"
                                        f"{combo}", "Current Item").title()

        # Ask user for new item name
        new_item = blank_checker(f"What would you like to change {item_change}"
                                 f" to?", "New Item").title()

        # Replace the current item name with new one
        new_combo[combo_name][new_item] = new_combo[combo_name].pop(
            item_change)

    elif change == "Price":

        # Ask user for name of current item which price needs to change
        price_change = blank_checker("Enter the name of the item's price you"
                                     " want to change\n\n"
                                     f"{name}\n\n"
                                     f"{combo}", "Current Item").title()

        # Give error message if item does not exist
        while price_change not in new_combo[combo_name]:
            easygui.msgbox(f"Sorry {price_change} is not in the original "
                           f"combo")

            # Keep asking user until valid item is entered
            price_change = blank_checker("Enter the name of the item's price you"
                                         " want to change\n\n"
                                         f"{name}\n\n"
                                         f"{combo}", "Current Item").title()

        # Ask user for new item price
        new_price = float_checker(f"What would you like to change "
                                  f"{price_change}'s price to?", 0, 40,
                                  "New Price")

        # Replace the current item price with new one
        new_combo[combo_name][price_change] = new_price
