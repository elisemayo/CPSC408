# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 2

class Menu:
    def __init__(self):
        pass

    def printMenu(self):
        print()
        print("~~~~~~~~~~~~~~~~~Menu~~~~~~~~~~~~~~~~~")
        print("1. Display all student records.\n"
        "2. Create student record.\n"
        "3. Update student record.\n"
        "4. Delete student record.\n"
        "5. Search student records.\n"
        "6. Quit")
        print()

    def choose(self):
        while True:
            try:
                choice = int(input("What would you like to do?\nChoose action: "))
                if choice > 6 or choice < 1:
                    raise Exception()
                break
            except Exception:
                print("Invalid menu option.")
        return choice