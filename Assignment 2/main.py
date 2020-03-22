# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 2

from DatabaseCRUD import CRUD
from Menu import Menu

if __name__ == "__main__":
    crud = CRUD("StudentDB.sqlite")
    menu = Menu()

    while True:
        menu.printMenu()
        action = menu.choose()

        if action == 1:
            crud.display()
        elif action == 2:
            crud.create()
        elif action == 3:
            crud.update()
        elif action == 4:
            crud.delete()
        elif action == 5:
            crud.search()
        elif action == 6:
            break
