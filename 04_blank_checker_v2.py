"""Version 2 of blank checker, puts code from v2 into a loop"""

import easygui

# Asks user for input
combo_name = easygui.enterbox("Enter combo name", "COMBO NAME")

while True:  # Loops until valid input is entered
    if combo_name == "":  # Checks if it's blank
        easygui.msgbox("You must fill out every field")  # Display error message
        combo_name = easygui.enterbox("Enter combo name", "COMBO NAME")

    else:
        easygui.msgbox(f"Combo name: {combo_name}")  # Display answer
        break
