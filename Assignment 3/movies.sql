-- Elise May
-- Student ID: 2271041
-- Email: may137@mail.chapman.edu
-- CPSC 408
-- Assignment 3

-- movie info (movieID, movieTitle, genre, ...)
CREATE TABLE IF NOT EXISTS MovieInfo(MovieID INT PRIMARY KEY AUTO_INCREMENT,
                        MovieTitle VARCHAR(32),
                        Genre VARCHAR(32),
                        Director VARCHAR(32),
                        Length DATETIME,
                        Actor1 VARCHAR(32),
                        Actor2 VARCHAR(32),
                        Actor3 VARCHAR(32),
                        Mood VARCHAR(32), 
                        UserRatings TINYINT);

-- user info (UserID, firstName, lastName)
CREATE TABLE IF NOT EXISTS UserInfo(UserID INT PRIMARY KEY AUTO_INCREMENT,
                        FirstName VARCHAR(32),
                        LastName VARCHAR(32));

-- user ratings (movieID, UserID, Rating, UserMood)
CREATE TABLE IF NOT EXISTS UserRating(MovieID INT PRIMARY KEY,
                        FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID),
                        UserID INT PRIMARY KEY,
                        FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                        Rating TINYINT,
                        UserMood VARCHAR(32));

-- user want to watch (userID, movieID, wantToWatch)
CREATE TABLE IF NOT EXISTS WantToWatch(UserID INT PRIMARY KEY,
                            FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                            MovieID INT,
                            FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID));

-- user watched (userID, movieID, Watched)
CREATE TABLE IF NOT EXISTS UserWatched(UserID INT PRIMARY KEY,
                            FOREIGN KEY (UserID) REFERENCES UserInfo(UserID),
                            MovieID INT,
                            FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID));
