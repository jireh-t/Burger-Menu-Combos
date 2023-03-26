"""Version 2 of welcome and menu screen, trialling it a different way using
easygui"""

import easygui

easygui.msgbox("Welcome to Burger Menu Combos")
choice = easygui.buttonbox("What would you like to do?\n", "Options",
                           choices=["1) Add combo","2) Search combo",
                                    "3) Delete combo","4) Output combo",
                                    "5) Exit"])
