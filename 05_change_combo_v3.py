"""Change combo component version 3, adding loops and formatting to each
option"""

import easygui

# Combo to change
new_combo = {"SUPER":
            {"Cheeseburger": 6.69,
             "Large Fries": 2.00,
             "Smoothie": 2.00}}

# Keep looping until the combo is correct
while True:

    # Print the combo and check with user that it is correct
    combo = ""
    for combo_name, combo_info in new_combo.items():
        name = f"{combo_name}"

        for food in combo_info:
            combo += f"{food}: {combo_info[food]}\n"

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
                               choices=["Combo name", "Item name",
                                        "Price"])

    if change == "Combo name":

        # Ask user for new combo name
        combo_name_change = easygui.enterbox("What would you like to "
                                             "change it to?").upper()

        # Replace the combo name with new name
        new_combo[combo_name_change] = new_combo.pop(combo_name)

    elif change == "Item name":

        # Ask user for current item they wish to change
        item_change = easygui.enterbox("Enter the name of the item you "
                                       "want to change\n\n"
                                       f"{name}\n\n"
                                       f"{combo}").title()

        # Give error message if item does not exist
        while item_change not in new_combo[combo_name]:
            easygui.msgbox(f"Sorry {item_change} is not in the original "
                           f"combo")

            # Keep asking user until valid item is entered
            item_change = easygui.enterbox("Enter the name of the item you "
                                           "want to change\n\n"
                                           f"{name}\n\n"
                                           f"{combo}").title()

        # Ask user for new item name
        new_item = easygui.enterbox(f"What would you like to change "
                                    f"{item_change} to?").title()

        # Replace the current item name with new one
        new_combo[combo_name][new_item] = new_combo[combo_name].pop(
            item_change)

    elif change == "Price":

        # Ask user for name of current item which price needs to change
        price_change = easygui.enterbox("Enter the name of the item's "
                                        "price you want to change\n\n"
                                        f"{name}\n\n"
                                        f"{combo}").title()

        # Give error message if item does not exist
        while price_change not in new_combo[combo_name]:
            easygui.msgbox(f"Sorry {price_change} is not in the original "
                           f"combo")

            # Keep asking user until valid item is entered
            price_change = easygui.enterbox("Enter the name of the item's "
                                            "price you want to change\n\n"
                                            f"{name}\n\n"
                                            f"{combo}").title()

        # Ask user for new item price
        new_price = easygui.enterbox(f"What would you like to change "
                                     f"{price_change}'s price to?")

        # Replace the current item price with new one
        new_combo[combo_name][price_change] = new_price
