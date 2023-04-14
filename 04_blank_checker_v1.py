"""Version 1 of blank checker, makes sure the input is not left blank"""

import easygui

# Asks user for input
combo_name = easygui.enterbox("Enter combo name", "COMBO NAME")

if combo_name == "":  # Checks if it's blank
    easygui.msgbox("You must fill out every field")  # Display error message

    # Asks again
    combo_name = easygui.enterbox("Enter combo name", "COMBO NAME")
    easygui.msgbox(f"Combo name: {combo_name}")  # Displays answer

else:
    easygui.msgbox(f"Combo name: {combo_name}")  # Display answer
