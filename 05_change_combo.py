import easygui


def change_combo(combo_confirm):
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
    if choice == "No":
        easygui.enterbox("Enter the item name you wish to change: ")
        if item in dictionary change, else repeat question


# Main Routine
new_combo = { "SUPER":
            {"Cheeseburger": 6.69,
             "Large fries": 2.00,
             "Smoothie": 2.00}}
change_combo(new_combo)
