# Stored Procdures for searches by single attributes
# (title, director, actor, streaming service, genre, mood)

CREATE PROCEDURE SearchTitle(IN title VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE MovieTitle LIKE CONCAT('%', title, '%');
END;

CREATE PROCEDURE SearchDirector(IN dir VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE Director LIKE CONCAT('%', dir, '%');
END;

CREATE PROCEDURE SearchActor(IN act VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE (Actor1 LIKE CONCAT('%', act, '%')
           OR Actor2 LIKE CONCAT('%', act, '%')
           OR Actor3 LIKE CONCAT('%', act, '%'));
END;

CREATE PROCEDURE SearchStreaming(IN service VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE SS.ServiceName LIKE service;
END;

CREATE PROCEDURE SearchGenre(IN gen VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE G.GenreTerm LIKE gen;
END;

CREATE PROCEDURE SearchMood(IN m VARCHAR(32))
BEGIN
    SELECT MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating, MI.MovieID
    FROM MovieInfo MI
    LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
    JOIN Genre G on MI.GenreID = G.GenreID
    JOIN Mood M on MI.MoodID = M.MoodID
    JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
    WHERE M.MoodTerm LIKE m;
END;


# Stored procedure for displaying a user's Want To Watch list
CREATE PROCEDURE WantToWatch(IN user INT)
BEGIN
   SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID
   FROM MovieInfo, UserWatchlist, Genre, Mood, StreamingService, avg_rating
   WHERE MovieInfo.MovieID = UserWatchlist.MovieID
     AND avg_rating.MovieID = MovieInfo.MovieID
     AND MovieInfo.MoodID = Mood.MoodID
     AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID
     AND MovieInfo.GenreID = Genre.GenreID
     AND UserID = user
     AND isDeleted = 0
     AND Watched = 0;
END;

# Stored procedure for displaying a user's Watched list
CREATE PROCEDURE Watched(IN user INT)
BEGIN
   SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, UserWatchlist.UserRating, MovieInfo.MovieID
   FROM MovieInfo, UserWatchlist, Genre, Mood, StreamingService
   WHERE MovieInfo.MovieID = UserWatchlist.MovieID
     AND MovieInfo.MoodID = Mood.MoodID
     AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID
     AND MovieInfo.GenreID = Genre.GenreID
     AND UserID = user
     AND isDeleted = 0
     AND Watched = 1;
END;

# Stored procedure for adding movie to user's Want to Watch list
CREATE PROCEDURE AddToWatchlist(IN user INT, IN movie INT)
BEGIN
    INSERT INTO UserWatchlist(UserID, MovieID, Watched, isDeleted)
    VALUES (user, movie, 0, 0);
END;

# Stored procedure for setting movie to watched, adding to Watched list
CREATE PROCEDURE SetToWatched(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET Watched = 1
    WHERE UserID = user AND MovieID = movie;
END;

# Stored procedure for deleting movie from Want To Watch list
CREATE PROCEDURE DeleteFromWatchlist(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET isDeleted = 1
    WHERE UserID = user AND MovieID = movie;
END;

# Stored procedure for deleting from Watched list
CREATE PROCEDURE DeleteFromWatched(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET Watched = 0
    WHERE UserID = user AND MovieID = movie;
END;

# Stored procedure for adding user's rating
CREATE PROCEDURE AddRating(IN user INT, IN movie INT, IN rating FLOAT)
BEGIN
    UPDATE UserWatchlist
    SET UserRating = rating
    WHERE UserID = user
    AND MovieID = movie;
END;

# Stored procedure for generating report of user's Watched list
CREATE PROCEDURE Report(IN user INT)
BEGIN
   SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, UserWatchlist.UserRating
   FROM MovieInfo, UserWatchlist, Genre, Mood, StreamingService
   WHERE MovieInfo.MovieID = UserWatchlist.MovieID
     AND MovieInfo.MoodID = Mood.MoodID
     AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID
     AND MovieInfo.GenreID = Genre.GenreID
     AND UserID = user
     AND isDeleted = 0
     AND Watched = 1;
END;

# Stored procedure for calculating user's total movies watched
CREATE PROCEDURE TotalMovies(IN user INT)
BEGIN
   SELECT COUNT(MovieID)
    FROM UserWatchlist
    WHERE UserID = user
   AND Watched = 1;
END;

# Stored procedure for selecting user's top rated movie
CREATE PROCEDURE TopMovie(IN user INT)
BEGIN
   SELECT MovieTitle, MAX(UserWatchlist.UserRating)
    FROM MovieInfo, UserWatchlist
    WHERE MovieInfo.MovieID = UserWatchlist.MovieID
    AND UserID = user
    AND Watched = 1
    GROUP BY MovieInfo.MovieID
    LIMIT 1;
END;

# Indexes for movie titles & actors
CREATE INDEX MovieTitle_Index ON MovieInfo(MovieTitle);
CREATE INDEX Actor_Index ON MovieInfo(Actor1,Actor2,Actor3);

CREATE VIEW `avg_rating` AS
    SELECT MovieID, ROUND(AVG(UserRating), 2) as Rating
    FROM UserWatchlist
    GROUP BY MovieID;
    
# Sub-query code for 2 searches on 2 different attributes (director/actor, genre/streaming service)
# **could not be implemented in Django/front-end
CREATE PROCEDURE search_dir_act(IN dir VARCHAR(32), IN act VARCHAR(32))
BEGIN
    SELECT MovieID, MovieTitle, Director, Actor1, GenreTerm, MoodTerm, ServiceName, Rating
    FROM(SELECT MI.MovieID, MovieTitle, Director, Actor1, Actor2, Actor3, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating
        FROM MovieInfo MI
        LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
        JOIN Genre G on MI.GenreID = G.GenreID
        JOIN Mood M on MI.MoodID = M.MoodID
        JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
        WHERE Director LIKE CONCAT('%', dir, '%')) as Directors
    WHERE (Actor1 LIKE CONCAT('%', act, '%')
           OR Actor2 LIKE CONCAT('%', act, '%')
           OR Actor3 LIKE CONCAT('%', act, '%'));
END;

CREATE PROCEDURE search_gen_str(IN gen VARCHAR(32), IN service VARCHAR(32))
BEGIN
    SELECT MovieID, MovieTitle, Director, Actor1, GenreTerm, MoodTerm, ServiceName, Rating
    FROM(SELECT MI.MovieID, MovieTitle, Director, Actor1, G.GenreTerm, M.MoodTerm, SS.ServiceName, IFNULL(a.Rating, 'Not Rated') as Rating
        FROM MovieInfo MI
        LEFT JOIN avg_rating a ON MI.MovieID = a.MovieID
        JOIN Genre G on MI.GenreID = G.GenreID
        JOIN Mood M on MI.MoodID = M.MoodID
        JOIN StreamingService SS on MI.StreamingServiceID = SS.StreamingServiceID
        WHERE SS.ServiceName LIKE service) as Services
    WHERE GenreTerm LIKE gen;
END;
