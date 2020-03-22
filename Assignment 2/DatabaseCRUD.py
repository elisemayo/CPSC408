# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 2

import sqlite3
from Student import Student


class CRUD:
    def __init__(self, db):
        # connect to database
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

        # create student table
        self.c.execute("CREATE TABLE IF NOT EXISTS Student("
                       "StudentId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "FirstName VARCHAR(32) NOT NULL,"
                       "LastName VARCHAR(32) NOT NULL,"
                       "GPA NUMERIC NOT NULL,"
                       "Major VARCHAR(16) NOT NULL,"
                       "FacultyAdvisor VARCHAR(32),"
                       "isDeleted SMALLINT)"
                       ";")
        self.conn.commit()

    def display(self):
        self.c.execute('SELECT * FROM Student WHERE isDeleted = 0')
        all_rows = self.c.fetchall()
        print(all_rows)

    def create(self):
        # collecting and validating inputs
        FirstName = input("First Name: ")
        while self.validate(FirstName) != True:
            print("Invalid entry.")
            FirstName = input("First Name: ")

        LastName = input("Last Name: ")
        while self.validate(LastName) != True:
            print("Invalid entry.")
            LastName = input("Last Name: ")

        GPA = input("GPA: ")
        while self.validateGPA(GPA) != True:
            print("Invalid entry. GPA must be numeric.")
            GPA = input("GPA: ")
        GPA = float(GPA)
        while GPA < 0.0 or GPA > 4.0:
            print("Invalid entry. GPA is limited to 4.0 scale.")
            GPA = input("GPA: ")
            while GPA.isdecimal() != True:
                print("Invalid entry. GPA must be numeric.")
                GPA = input("GPA: ")
            GPA = float(GPA)

        Major = input("Major: ")
        while self.validate(Major) != True:
            print("Invalid entry.")
            Major = input("Major: ")

        FacultyAdvisor = input("Faculty Advisor: ")
        while self.validate(FacultyAdvisor) != True:
            print("Invalid entry.")
            FacultyAdvisor = input("Faculty Advisor: ")

        isDeleted = 0

        # write to database
        student = Student(FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted)
        self.c.execute("INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted) "
                       "VALUES(?,?,?,?,?,?);", student.getValues())
        self.conn.commit()
        print("Student record created.")

    def update(self):
        studID = input("Student ID: ")
        select = ""
        # validate student ID input
        while self.validateID(studID) != True:
            print("Invalid entry. Student ID must be numeric.")
            studID = input("Student ID: ")
        # validate whether student is in database
        studID = int(studID)

        if self.validateStudent(studID) is True:
            while True:
                select = input("Would you like to update the student's major or faculty advisor?\n"
                               "Type 'Major' or 'Advisor': ")
                if select.lower() == 'major':
                    select = "Major"
                    break
                elif select.lower() == 'advisor':
                    select = "FacultyAdvisor"
                    break
                else:
                    print("Invalid option. Try again.")
            update = input("Enter the new value: ")

            # write to database
            self.c.execute("UPDATE Student SET {0} = '{1}' WHERE StudentId = {2};".format(select, update, studID))
            self.conn.commit()
            print("UPDATE COMPLETE")
        else:
            print("UPDATE FAILED")

    def delete(self):
        studID = input("Student ID: ")
        # validate student ID input
        while self.validateID(studID) != True:
            print("Invalid entry. Student ID must be numeric.")
            studID = input("Student ID: ")

        if self.validateStudent(studID) is True:
            self.c.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1, studID,))
            self.conn.commit()
            print("DELETE COMPLETE")
        else:
            print("DELETE FAILED")

    def search(self):
        while True:
            select = input("Search by:\n"
                           "Major\n"
                           "GPA\n"
                           "Faculty Advisor\n"
                           "Type 'Major', 'GPA', or 'Advisor': ")
            if select.lower() == 'major':
                select = "Major"
                break
            elif select.lower() == 'gpa':
                select = "GPA"
                break
            elif select.lower() == 'advisor':
                select = "FacultyAdvisor"
                break
            else:
                print("Invalid option. Try again.")

        search = input("Enter search term: ")
        # validating search terms and retrieving data
        if select == "Major":
            while self.validate(search) != True:
                print("Invalid syntax. Try again.")
                search = input("Enter search term: ")
            self.c.execute('SELECT * FROM Student WHERE isDeleted = 0 AND Major = ?', (search,))
            all_rows = self.c.fetchall()
            if len(all_rows) == 0:
                print("No records found.")
            else:
                print(all_rows)
        elif select == "GPA":
            while self.validateGPA(search) != True:
                print("Invalid syntax. Try again.")
                search = input("Enter search term: ")
            self.c.execute('SELECT * FROM Student WHERE isDeleted = 0 AND GPA = ?', (search,))
            all_rows = self.c.fetchall()
            if len(all_rows) == 0:
                print("No records found.")
            else:
                print(all_rows)
        elif select == "FacultyAdvisor":
            while self.validate(search) != True:
                print("Invalid syntax. Try again.")
                search = input("Enter search term: ")
            self.c.execute('SELECT * FROM Student WHERE isDeleted = 0 AND FacultyAdvisor = ?', (search,))
            all_rows = self.c.fetchall()
            if len(all_rows) == 0:
                print("No records found.")
            else:
                print(all_rows)

    # validate inputs to account for spaces
    def validate(self, input):
        if all(i.isalpha() or i.isspace() for i in input):
            isValid = True
        else:
            isValid = False
        return isValid

    def validateGPA(self, input):
        if all(i.isdecimal() for i in input) or "." in input:
            isValid = True
        else:
            isValid = False
        return isValid

    def validateID(self, input):
        if all(i.isdecimal() for i in input):
            isValid = True
        else:
            isValid = False
        return isValid

    def validateStudent(self, studID):
        self.c.execute("SELECT StudentID FROM Student WHERE StudentId = ?",
                       (studID,))
        data = self.c.fetchall()
        if len(data) > 0:
            return True
        else:
            print("Student not found.")
            return False
