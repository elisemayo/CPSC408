# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 2

class Student:
    def __init__(self, FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted):
        self.FirstName = str(FirstName)
        self.LastName = str(LastName)
        self.GPA = float(GPA)
        self.Major = str(Major)
        self.FacultyAdvisor = str(FacultyAdvisor)
        self.isDeleted = int(isDeleted)

    # getters
    def getValues(self):
        return (self.FirstName, self.LastName, self.GPA, self.Major, self.FacultyAdvisor, self.isDeleted)

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getGPA(self):
        return self.GPA

    def getMajor(self):
        return self.Major

    def getFacultyAdvisor(self):
        return self.FacultyAdvisor

    def getisDeleted(self):
        return self.isDeleted

    # setters
    def setFirstName(self, name):
        self.FirstName = str(name)

    def setLastName(self, name):
        self.LastName = str(name)

    def setGPA(self, GPA):
        self.GPA = float(GPA)

    def setMajor(self, Major):
        self.Major = str(Major)

    def setFacultyAdvisor(self, FacultyAdvisor):
        self.FacultyAdvisor = str(FacultyAdvisor)

    def setisDeleted(self, isDeleted):
        self.isDeleted = int(isDeleted)