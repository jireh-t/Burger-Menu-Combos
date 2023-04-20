"""Trial 2 to output the menu in separate boxes"""

import easygui

# Stored combos
combo_menu = {"VALUE":
            {"Beef Burger": "5.69",
             "Fries": "1.00",
             "Fizzy Drink": "1.00"},
          "CHEEZY":
            {"Cheeseburger": "6.69",
             "Fries": "1.00",
             "Fizzy Drink": "1.00"},
          "SUPER":
            {"Cheeseburger": "6.69",
             "Large Fries": "2.00",
             "Smoothie": "2.00"}
          }

info = ""

# Loop to print combo name
for combo_name, combo_info in combo_menu.items():

    # Print the combo items and price
    for key, value in combo_info.items():
        info += f"{key}: {value} \n"

    # Output in separate message boxes
    easygui.msgbox(f"{combo_name}\n"
               f"{info}", "MENU")

    # Clear the info for the next combo
    info = ""


