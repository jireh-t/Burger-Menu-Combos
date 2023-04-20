"""Trial 2, to delete a combo using pop"""

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
choice = easygui.enterbox(f"/ / / Below is the full menu of combos/ / /\n\n"
                          f"{menu}\n\n"
                          "Which combo would you like to delete?").upper()

# Show error message if the combo is not in the menu

while choice not in combos:
    easygui.msgbox(f"Sorry, {choice} is not in the menu", "ERROR")

    # Output the full menu and ask the user what combo to delete
    choice = easygui.enterbox(f"/ / / Below is the full menu of combos/ / /\n\n"
                              f"{menu}\n\n"
                              "Which combo would you like to delete?",
                              "ENTER COMBO NAME").upper()

# Delete the combo
pop = combos.pop(choice)
easygui.msgbox(f"{choice} has been deleted", "DELETED")

print(combos)
