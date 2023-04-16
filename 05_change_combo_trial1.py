import easygui


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


def change_combo(combo_confirm):
    while True:

        # Print the combo and check with user that it is correct
        combo = ""
        for combo_name, combo_info in combo_confirm.items():
            name = f"{combo_name}"

            for food in combo_info:
                combo += f"{food}: {combo_info[food]}\n"

        choice = easygui.buttonbox(f"/ / / Is the following combo correct? / / "
                                   f"/\n\n"
                                   f"{name}\n\n"
                                   f"{combo}",
                                   "PLEASE CONFIRM",
                                   choices=["Yes", "No"])

        if choice == "Yes":
            break

        change = easygui.buttonbox("What would you like to change?",
                                   choices=["Combo name", "Item name",
                                            "Price"])

        if change == "Combo name":
            combo_name_change = easygui.enterbox("What would you like to "
                                                 "change it to?")

            combo_confirm[combo_name_change] = combo_confirm.pop(combo_name)

            easygui.msgbox(combo_confirm)

        elif change == "Item name":
            item_change = easygui.enterbox("Enter the name of the item you "
                                           "want to change\n\n"
                                           f"{name}\n\n"
                                           f"{combo}")

            while item_change not in combo_confirm[combo_name]:
                easygui.msgbox(f"Sorry {item_change} is not in the original "
                               f"combo")
                item_change = easygui.enterbox("Enter the name of the item you"
                                               " want to change\n\n"
                                               f"{name}\n\n"
                                               f"{combo}")

            new_item = easygui.enterbox(f"What would you like to change "
                                        f"{item_change} to?")

            combo_confirm[combo_name][new_item] = combo_confirm[
                combo_name].pop(item_change)

            print(combo_confirm)


        elif change == "Price":
            price_change = easygui.enterbox("Enter the name of the item's "
                                            "price you want to change\n\n"
                                            f"{name}\n\n"
                                            f"{combo}")

            while price_change not in combo_confirm[combo_name]:
                easygui.msgbox(f"Sorry {price_change} is not in the original "
                f"combo")
                price_change = easygui.enterbox("Enter the name of the item's "
                                                "price you want to change\n\n"
                                                f"{name}\n\n"
                                                f"{combo}")

            new_price = easygui.enterbox(f"What would you like to change "
                                         f"{price_change}'s price to?")

            combo_confirm[combo_name][price_change] = new_price
            easygui.msgbox(combo_confirm)


# Main Routine
new_combo = {"SUPER":
            {"Cheeseburger": 6.69,
             "Large fries": 2.00,
             "Smoothie": 2.00}}

change_combo(new_combo)
