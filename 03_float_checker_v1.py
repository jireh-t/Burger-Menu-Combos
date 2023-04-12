"""Component 3 Float Checker version1
Makes sure the user has entered a price in between $0 and $40"""

import easygui


price = float(easygui.enterbox("Enter price", "Price"))

# Keep asking until a valid amount (0-40) is entered
while not 0 < price <= 40:
    easygui.msgbox("Try again. Please enter a price between $0 and $40")
    # Ask user for input
    price = float(easygui.enterbox("Enter price", "Price"))

easygui.msgbox(f"Price is ${price:.2f}")
