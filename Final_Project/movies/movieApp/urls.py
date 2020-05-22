# Elise May & Nicole Chu
# CPSC 408 Final Project

# from django.conf.urls import url
from django.urls import path
from movieApp import views
from .views import HomePageView, SearchView, WantToWatchView, WatchedView, ResultsView, RateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'search/', SearchView.as_view(), name='search'),
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), {'next_page': '/accounts/login'}, name='logout'),
    path(r'wanttowatch/', views.WantToWatchView, name='wanttowatch'),
    path(r'watched/', views.WatchedView, name='watched'),
    path(r'register/', views.register, name='register'),
    path(r'results/', views.ResultsView, name='results'),
    path(r'rate/', views.RateView, name='rate'),
    path(r'watched/submit', views.RemoveWatched, name='removewatched'),
    path(r'results/submit', views.AddToWatchlist, name='addtowatchlist'),
    path(r'wanttowatch/submit', views.WantToWatchActions, name='wanttowatchactions'),
    path(r'export/', views.Reporting, name='export'),
]