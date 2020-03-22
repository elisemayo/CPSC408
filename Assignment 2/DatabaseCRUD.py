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
        # self.c.execute("CREATE TABLE IF NOT EXISTS Student("
        #             "StudentId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
        #             "FirstName VARCHAR(32) NOT NULL,"
        #             "LastName VARCHAR(32) NOT NULL,"
        #             "GPA NUMERIC NOT NULL,"
        #             "Major VARCHAR(16) NOT NULL,"
        #             "FacultyAdvisor VARCHAR(32),"
        #             "isDeleted SMALLINT)"
        #             ");")
        self.conn.commit()

    def display(self):
        self.c.execute('SELECT * FROM Student')
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

    # def update(self):
    #     # update
    #
    # def delete(self):
    #     # delete
    #
    # def search(self):
    #     # search

    #validate inputs to account for spaces
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