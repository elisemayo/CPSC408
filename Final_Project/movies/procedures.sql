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

CREATE PROCEDURE AddToWatchlist(IN user INT, IN movie INT)
BEGIN
    INSERT INTO UserWatchlist(UserID, MovieID, Watched, isDeleted)
    VALUES (user, movie, 0, 0);
END;

CREATE PROCEDURE SetToWatched(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET Watched = 1
    WHERE UserID = user AND MovieID = movie;
END;

CREATE PROCEDURE DeleteFromWatchlist(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET isDeleted = 1
    WHERE UserID = user AND MovieID = movie;
END;

CREATE PROCEDURE DeleteFromWatched(IN user INT, IN movie INT)
BEGIN
    UPDATE UserWatchlist
    SET Watched = 0
    WHERE UserID = user AND MovieID = movie;
END;

CREATE PROCEDURE AddRating(IN user INT, IN movie INT, IN rating FLOAT)
BEGIN
    UPDATE UserWatchlist
    SET UserRating = rating
    WHERE UserID = user
    AND MovieID = movie;
END;

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

CREATE PROCEDURE TotalMovies(IN user INT)
BEGIN
   SELECT COUNT(MovieID)
    FROM UserWatchlist
    WHERE UserID = user
   AND Watched = 1;
END;

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

CREATE INDEX MovieTitle_Index ON MovieInfo(MovieTitle);
CREATE INDEX Actor_Index ON MovieInfo(Actor1,Actor2,Actor3);

CREATE VIEW `avg_rating` AS
    SELECT MovieID, ROUND(AVG(UserRating), 2) as Rating
    FROM UserWatchlist
    GROUP BY MovieID;