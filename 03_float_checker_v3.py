"""Component 3 float checker v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

import easygui

# Main routine
error = "Try again. Please enter a price between $0 and $40\n"
price = 0

# Keep asking until a valid amount (0-40) is entered
while not 0 < price <= 40:
    try:
        # Ask for amount
        price = float(easygui.enterbox("Enter price", "Price"))

    except ValueError:
        easygui.msgbox(error)

easygui.msgbox(f"Price is ${price:.2f}")

