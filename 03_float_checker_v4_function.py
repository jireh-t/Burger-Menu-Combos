"""Component 3 Float Checker function
Change v3 into a function"""

import easygui


# Float checking function - loops until a valid number is entered
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
                return number
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error, "Error")


# Main routine
price = float_checker("Please enter price of burger", 0, 40, "Burger")
price = f"{price:.2f}"
easygui.msgbox(f" Burger = ${price}")
