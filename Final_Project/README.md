# Movie Database

Full Name: Elise May & Nicole Chu
Student ID: 2271041, 2290152 
Chapman Email: may137@mail.chapman.edu, nichu@chapman.edu
Course Number and Section: CPSC 408-01
Assignment or Exercise Number: Final Project - Movie Database

Source Files
SQL files:
a. procedures.sql
b. schema.sql

HTML/CSS files (templates):
a. base.html
b. index.html
c. profile.html
d. rate.html
e. results.html
f. wanttowatch.html
g. watched.html
h. css/searchbar.css

Django files:
a. movieApp/__init__.py
b. movieApp/admin.py
c. movieApp/apps.py
d. movieApp/forms.py
e. movieApp/models.py
f. movieApp/tests.py
g. movieApp/urls.py
h. movieApp/views.py
i. movies/movies/__init__.py
j. movies/movies/asgi.py
k. movies/movies/settings.py
l. movies/movies/urls.py
m. movies/movies/wsgi.py
n. movies/manage.py

A DESCRIPTION OF ANY KNOWN COMPILE OR RUNTIME ERRORS, CODE LIMITATIONS, OR DEVIATIONS FROM ASSIGNMENT SPECIFICATIONS
a. Subqueries included in procedures.sql but not fully implemented on front-end.
b. Rating request.POST.get('rating') in RateView call stops working sometimes...

A LIST OF ALL REFERENCES USED TO COMPLETE THE ASSIGNMENT, INCLUDING PEERS (IF APPLICABLE)
a. https://pynative.com/python-mysql-execute-stored-procedure/
b. https://database.guide/4-ways-to-replace-null-with-a-different-value-in-mysql/
c. https://www.guru99.com/views.html

INSTRUCTIONS FOR RUNNING THE ASSIGNMENT
a. Navigate to path/movies folder
b. Run python manage.py runserver
