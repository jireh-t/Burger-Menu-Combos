"""Component 3 Float Checker version2
Use try/except and pull error message out of the loop"""


import easygui

error = easygui.msgbox("Try again. Please enter a price between $0 and $40")
valid = False

# Keep asking until a valid amount (0-40) is entered
while not valid:
    try:
        # Ask for amount
        price = float(easygui.enterbox("Enter price", "Price"))

        # Check if the amount is too high or too low
        if 0 < price <= 40:
            easygui.msgbox(f"Price is ${price:.2f}")
            valid = True
        else:
            easygui.msgbox(error)

    except ValueError:
        easygui.msgbox(error)




