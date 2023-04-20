"""Version 4 of component 8 to output menu, putting into a function"""

import easygui
from math import fsum


# Function to output the whole menu
def output_combo(combos):

    menu = ""

    # Loop to print full menu
    for combo_name, combo_info in combos.items():

        # Print the combo name
        menu += f"\n{combo_name}\n"

        # Print the combo items and price
        for key, value in combo_info.items():
            menu += f"{key}: ${value:.2f} \n"

        total = fsum(combos[combo_name].values())
        menu += f"\nTotal: ${total:.2f}\n"
        menu += "---------------------------------------"

    # Output the full menu and ask the user what combo to delete
    easygui.msgbox(f"/ / / Below is the full menu of combos/ / /\n\n"
                f"{menu}\n\n", "MENU")


# Main Routine

# Stored combos
combo_menu = {"VALUE":
            {"Beef Burger": 5.69,
             "Fries": 1.00,
             "Fizzy Drink": 1.00},
          "CHEEZY":
            {"Cheeseburger": 6.69,
             "Fries": 1.00,
             "Fizzy Drink": 1.00},
          "SUPER":
            {"Cheeseburger": 6.69,
             "Large Fries": 2.00,
             "Smoothie": 2.00}
          }

output_combo(combo_menu)
