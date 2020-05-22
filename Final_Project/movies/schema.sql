CREATE TABLE IF NOT EXISTS StreamingService(StreamingServiceID INT PRIMARY KEY AUTO_INCREMENT,
                                            ServiceName VARCHAR(32));

CREATE TABLE IF NOT EXISTS Mood(MoodID INT PRIMARY KEY AUTO_INCREMENT,
                                MoodTerm VARCHAR(32));
								
CREATE TABLE IF NOT EXISTS Genre(GenreID INT PRIMARY KEY AUTO_INCREMENT,
                                GenreTerm VARCHAR(32));
								
CREATE TABLE IF NOT EXISTS MovieInfo(MovieID INT PRIMARY KEY AUTO_INCREMENT,
                                    MovieTitle VARCHAR(32),
                                    GenreID INT,
                                        FOREIGN KEY (GenreID) REFERENCES Genre(GenreID),
                                    Director VARCHAR(32),
                                    Length INT,
                                    Actor1 VARCHAR(32),
                                    Actor2 VARCHAR(32),
                                    Actor3 VARCHAR(32),
                                    StreamingServiceID INT,
                                        FOREIGN KEY (StreamingServiceID) REFERENCES StreamingService(StreamingServiceID),
                                    MoodID INT,
                                        FOREIGN KEY (MoodID) REFERENCES Mood(MoodID));
										
CREATE TABLE IF NOT EXISTS UserWatchlist(UserID INT,
                                            FOREIGN KEY (UserID) REFERENCES auth_user(id),
                                        MovieID INT,
                                            FOREIGN KEY (MovieID) REFERENCES MovieInfo(MovieID),
                                        Watched BIT,
                                        UserRating FLOAT,
                                        isDeleted BIT,
                                        updated_at TIMESTAMP NOT NULL
                                            DEFAULT CURRENT_TIMESTAMP
                                            ON UPDATE CURRENT_TIMESTAMP,
                                        PRIMARY KEY(UserID, MovieID));										
								
INSERT INTO StreamingService(ServiceName)
VALUE ('Netflix');
INSERT INTO StreamingService(ServiceName)
VALUE ('Hulu');
INSERT INTO StreamingService(ServiceName)
VALUE ('Prime Video');
INSERT INTO StreamingService(ServiceName)
VALUE ('Disney+');
INSERT INTO StreamingService(ServiceName)
VALUE ('Apple TV+');

INSERT INTO Mood(MoodTerm)
VALUE ('thought-provoking');
INSERT INTO Mood(MoodTerm)
VALUE ('funny');
INSERT INTO Mood(MoodTerm)
VALUE ('feel-good');
INSERT INTO Mood(MoodTerm)
VALUE ('sad');
INSERT INTO Mood(MoodTerm)
VALUE ('scared');
INSERT INTO Mood(MoodTerm)
VALUE ('romantic');
INSERT INTO Mood(MoodTerm)
VALUE ('thrilling');

INSERT INTO Genre(GenreTerm)
VALUE ('Action');
INSERT INTO Genre(GenreTerm)
VALUE ('Sci-Fi');
INSERT INTO Genre(GenreTerm)
VALUE ('Comedy');
INSERT INTO Genre(GenreTerm)
VALUE ('Romance');
INSERT INTO Genre(GenreTerm)
VALUE ('Horror');
INSERT INTO Genre(GenreTerm)
VALUE ('Thriller');
INSERT INTO Genre(GenreTerm)
VALUE ('Documentary');
INSERT INTO Genre(GenreTerm)
VALUE ('Western');
INSERT INTO Genre(GenreTerm)
VALUE ('Rom-Com');
INSERT INTO Genre(GenreTerm)
VALUE ('Mystery');
INSERT INTO Genre(GenreTerm)
VALUE ('Musical');
INSERT INTO Genre(GenreTerm)
VALUE ('Drama');
INSERT INTO Genre(GenreTerm)
VALUE ('Documentary');
INSERT INTO Genre(GenreTerm)
VALUE ('Fantasy');
INSERT INTO Genre(GenreTerm)
VALUE ('Adventure');