"""Component 3 Float Checker version2
Develops a float checker function to ensure the user has entered a valid
price"""

import easygui


# Float checking function - loops until a valid number is entered
def float_checker(question, item):
    error = "\nSorry, you must enter a valid price\n"
    while True:
        try:
            number = float(easygui.enterbox(question, item))
            return number
        except ValueError:
            easygui.msgbox(error, "Error")


# Main routine
price = float_checker("Please enter price of burger", "Burger")
price = f"{price:.2f}"
print(f" Burger = ${price}")
