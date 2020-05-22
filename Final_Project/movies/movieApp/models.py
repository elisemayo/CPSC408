from django.db import models

class Movie(models.Model):
    title = models.CharField(db_column='MovieTitle', max_length=32, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=32, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=32, blank=True, null=True)  # Field name made lowercase.

class Movieinfo(models.Model):
    movieid = models.AutoField(db_column='MovieID', primary_key=True)  # Field name made lowercase.
    movietitle = models.CharField(db_column='MovieTitle', max_length=32, blank=True, null=True)  # Field name made lowercase.
    genreid = models.IntegerField(db_column='GenreID', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=32, blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    actor1 = models.CharField(db_column='Actor1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    actor2 = models.CharField(db_column='Actor2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    actor3 = models.CharField(db_column='Actor3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    streaming = models.IntegerField(db_column='StreamingServiceID', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='UserRating', blank=True, null=True)  # Field name made lowercase.
    mood = models.IntegerField(db_column='MoodID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieInfo'

class Genre(models.Model):
    genreid = models.AutoField(db_column='GenreID', primary_key=True)  # Field name made lowercase.
    genreterm = models.CharField(db_column='GenreTerm', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genre'

class Mood(models.Model):
    moodid = models.AutoField(db_column='MoodID', primary_key=True)  # Field name made lowercase.
    moodterm = models.CharField(db_column='MoodTerm', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mood'

class Streamingservice(models.Model):
    streamingserviceid = models.AutoField(db_column='StreamingServiceID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StreamingService'



