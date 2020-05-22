# Elise May & Nicole Chu
# CPSC 408 Final Project

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from movieApp.forms import SignUpForm, SearchForm, RateForm
from django.db import connection
import csv
from django.http import HttpResponse
import pandas as pd

class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchView(TemplateView):
    template_name = 'index.html'

# class RateView(TemplateView):
#     template_name = 'rate.html'

# class WantToWatch(TemplateView):
#     template_name = 'wanttowatch.html'
#
# class WatchedView(TemplateView):
#     template_name = 'watched.html'

class LoginView(TemplateView):
    template_name = '/registration/login.html'

class LogoutView(TemplateView):
    template_name = '/registration/logged_out.html'

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def sql_query(proc,param):
    try:
        with connection.cursor() as cursor:
            cursor.callproc(proc, [param])
            results = cursor.fetchall()
    except Exception as E:
        print(str(E))
        connection.rollback()
    return results

@login_required
def ResultsView(request):
    title = request.POST.get('title')
    director = request.POST.get('director')
    actor = request.POST.get('actor')
    streaming = request.POST.get('streaming')
    genre = request.POST.get('genre')
    mood = request.POST.get('mood')
    length = request.POST.get('length')
    rating = request.POST.get('rating')
    if title:
        myresults = sql_query('SearchTitle',title)
    elif director:
        myresults = sql_query('SearchDirector',director)
    elif actor:
        myresults = sql_query('SearchActor',actor)
    elif streaming:
        myresults = sql_query('SearchStreaming',streaming)
    elif genre:
        myresults = sql_query('SearchGenre',genre)
    elif mood:
        myresults = sql_query('SearchMood',mood)
    elif length:
        with connection.cursor() as cursor:
            if length == "less than 1.5 hours":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE Length < 90 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif length == "1.5-2 hours":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE (Length = 90 OR Length = 120 OR (Length > 90 AND Length < 120)) "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif length == "2-3 hours":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE (Length = 120 OR Length = 180 OR (Length > 120 AND Length < 180)) "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif length == "3 hours +":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE (Length = 180 OR Length > 180) "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            myresults = cursor.fetchall()
    elif rating:
        with connection.cursor() as cursor:
            if rating == "less than 1 star":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE avg_rating.Rating < 1 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif rating == "1-1.99 stars":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE avg_rating.Rating >= 1 AND avg_rating.Rating < 2 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif rating == "2-2.99 stars":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE avg_rating.Rating >= 2 AND avg_rating.Rating < 3 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif rating == "3-3.99 stars":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE avg_rating.Rating >= 3 AND avg_rating.Rating < 4 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            elif rating == "4-5 stars":
                cursor.execute(
                    "SELECT MovieTitle, Director, Actor1, Genre.GenreTerm, Mood.MoodTerm, StreamingService.ServiceName, avg_rating.Rating, MovieInfo.MovieID "
                    "FROM MovieInfo, Mood, StreamingService, Genre, avg_rating "
                    "WHERE avg_rating.Rating >= 4 "
                    "AND avg_rating.MovieID = MovieInfo.MovieID "
                    "AND MovieInfo.MoodID = Mood.MoodID "
                    "AND MovieInfo.StreamingServiceID = StreamingService.StreamingServiceID "
                    "AND MovieInfo.GenreID = Genre.GenreID ")
            myresults = cursor.fetchall()
    return render(request, 'results.html', {'myresults': myresults})

@login_required
def WantToWatchView(request):
    user = request.user.id
    watchlist = sql_query('WantToWatch', user)
    return render(request, 'wanttowatch.html', {'watchlist': watchlist})

@login_required
def WatchedView(request):
    user = request.user.id
    watched = sql_query('Watched', user)
    return render(request, 'watched.html', {'watched': watched})

def RateView(request):
    user = request.user.id
    rating = request.POST.get('rating')
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT MovieID "
                "FROM UserWatchlist "
                "ORDER BY UserWatchlist.updated_at DESC "
                "LIMIT 1 "
            )
            tuple = cursor.fetchone()
            movie = tuple[0]
    except Exception as E:
        print(str(E))
        connection.rollback()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('AddRating', [user,movie,rating])
    except Exception as E:
        print(str(E))
        connection.rollback()
    return render(request, 'rate.html')

def AddToWatchlist(request):
    user = request.user.id
    movie = request.POST.get('wanttowatch')
    try:
        with connection.cursor() as cursor:
            cursor.callproc('AddToWatchlist', [user,movie])
    except Exception as E:
        print(str(E))
        connection.rollback()
    watchlist = sql_query('WantToWatch', user)
    return render(request, 'wanttowatch.html',{'watchlist': watchlist})

def WantToWatchActions(request):
    user = request.user.id
    # user watched the movie
    if 'watched' in request.POST:
        user = request.user.id
        movie = request.POST.get('watched')
        try:
            with connection.cursor() as cursor:
                cursor.callproc('SetToWatched', [user, movie])
        except Exception as E:
            print(str(E))
            connection.rollback()
        return redirect('rate')
    # user wants to remove from watchlist
    elif 'delete' in request.POST:
        user = request.user.id
        movie = request.POST.get('delete')
        try:
            with connection.cursor() as cursor:
                cursor.callproc('DeleteFromWatchlist', [user, movie])
        except Exception as E:
            print(str(E))
            connection.rollback()
        return redirect('wanttowatch')
    watchlist = sql_query('WantToWatch', user)
    return render(request, 'wanttowatch.html', {'watchlist': watchlist})

def RemoveWatched(request):
    user = request.user.id
    movie = request.POST.get('delete')
    try:
        with connection.cursor() as cursor:
            cursor.callproc('DeleteFromWatched', [user,movie])
    except Exception as E:
        print(str(E))
        connection.rollback()
    watched = sql_query('Watched', user)
    return render(request, 'watched.html',{'watched': watched})

def Reporting(request):
    user = request.user.id
    watched = sql_query('Report', user)
    tuple = sql_query('TotalMovies', user)
    totalMovies = tuple[0][0]
    toptuple = sql_query('TopMovie', user)
    topMovie = toptuple[0][0]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="watched.csv"'
    data = pd.DataFrame(watched, columns=['MovieTitle','Director','Actor1','Genre','Mood','Streaming','UserRating'])
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Movie Title','Director','Lead Actor','Genre','Mood','Streaming','Your Rating'])
    for row in data.itertuples():
        writer.writerow([row.MovieTitle, row.Director, row.Actor1, row.Genre, row.Mood,
                         row.Streaming, row.UserRating])
    writer.writerow(['Total Number of Movies Watched:', totalMovies])
    writer.writerow(['Your Top Rated Movie:', topMovie])
    return response