"""Trial 1 of component 8 to output menu, printing the whole menu at once"""

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

menu = ""

# Loop to print full menu
for combo_name, combo_info in combo_menu.items():

    # Print the combo name
    menu += f"\n{combo_name}\n"

    # Print the combo items and price
    for key, value in combo_info.items():
        menu += f"{key}: {value} \n"

# Output the full menu
easygui.msgbox(f"/ / / Below is the full menu of combos/ / /\n\n"
            f"{menu}\n\n")
