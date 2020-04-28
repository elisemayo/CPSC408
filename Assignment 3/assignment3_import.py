# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 3

import csv
import mysql.connector

# connecting to database
config = {
    'host': '35.247.88.39',
    'user': 'root',
    'passwd': 'DatabaseIsSexy69',
    'database': 'movies'
}

# connection object
db = mysql.connector.connect(**config)

mycursor = db.cursor()
file_name = input("CSV File Name (ex: 'file_name.csv'): ")

with open(file_name, newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

    for row in file_reader:
        # MovieInfo
        if row[0] == '1':
            # movieID attribute auto-increments
            title = row[2]
            genre = row[3]
            director = row[4]
            length = row[5]
            actor1 = row[6]
            actor2 = row[7]
            actor3 = row[8]
            mood = row[9]
            rating = row[10]
            input_param = (title, genre, director, length, actor1, actor2, actor3, mood, rating)
            mycursor.execute(
                "INSERT INTO MovieInfo(MovieTitle, Genre, Director, Length, Actor1, Actor2, Actor3, Mood, UserRatings)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", input_param)
            db.commit()

        # UserInfo
        elif row[0] == '2':
            # userID auto-increments
            first = row[2]
            last = row[3]
            input_param = (first, last)
            mycursor.execute("INSERT INTO UserInfo(FirstName, LastName)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

        # UserRating
        elif row[0] == '3':
            movieID = row[1]
            userID = row[2]
            rating = row[3]
            mood = row[4]
            input_param = (movieID, userID, rating, mood)
            mycursor.execute("INSERT INTO UserRating(MovieID, UserID, Rating, UserMood)"
                             "VALUES (%s, %s, %s, %s)", input_param)
            db.commit()

        # WantToWatch
        elif row[0] == '4':
            userID = row[1]
            movieID = row[2]
            input_param = (userID, movieID)
            mycursor.execute("INSERT INTO WantToWatch(UserID, MovieID)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

        # UserWatched
        elif row[0] == '5':
            userID = row[1]
            movieID = row[2]
            input_param = (userID, movieID)
            mycursor.execute("INSERT INTO UserWatched(UserID, MovieID)"
                             "VALUES (%s, %s)", input_param)
            db.commit()

db.close()
