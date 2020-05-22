# Elise May & Nicole Chu
# CPSC 408 Final Project

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, ChoiceField
from .models import Movieinfo

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SearchForm(forms.Form):
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('sci-fi', 'Sci-Fi'),
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('thriller', 'Thriller'),
        ('documentary', 'Documentary'),
        ('western', 'Western'),
        ('rom-com', 'Rom-Com'),
        ('mystery', 'Mystery'),
        ('musical', 'Musical'),
        ('drama', 'Drama'),
        ('animated', 'Animated'),
        ('fantasy', 'Fantasy'),
        ('adventure', 'Adventure'),
    )
    MOOD_CHOICES = (
        ('thought-provoking', 'Thought-Provoking'),
        ('funny', 'Funny'),
        ('feel-good', 'Feel-Good'),
        ('sad', 'Sad'),
        ('scared', 'Scared'),
        ('romantic', 'Romantic'),
        ('thrilling', 'Thrilling'),
    )
    LENGTH_CHOICES = (
        ('less than 1.5 hours', 'LESS THAN 1.5 HOURS'),
        ('1.5-2 hours', '1.5-2 HOURS'),
        ('2-3 hours', '2-3 HOURS'),
        ('3 hours +', '3 HOURS +'),
    )
    RATING_CHOICES = (
        ('less than 1 star', 'LESS THAN 1 STAR'),
        ('1-1.99 stars', '1-1.99 STARS'),
        ('2-2.99 stars', '2-2.99 STARS'),
        ('3-3.99 stars', '3-3.99 STARS'),
        ('4-5 stars', '4-5 STARS'),
    )
    title = forms.CharField(max_length=30, required=False)
    actor = forms.CharField(max_length=30, required=False)
    director = forms.CharField(max_length=30, required=False)
    streaming = forms.CharField(max_length=30, required=False)
    genre = forms.ChoiceField(choices=GENRE_CHOICES, required=False)
    mood = forms.ChoiceField(choices=MOOD_CHOICES, required=False)
    length = forms.ChoiceField(choices=LENGTH_CHOICES, required=False)
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=False)

    class Meta:
        model = Movieinfo
        fields = ('title', 'actor', 'director', 'streaming', 'genre', 'mood', 'length', 'rating',)

class RateForm(forms.Form):
    RATING_CHOICES = (
        ('1 star', 'STAR'),
        ('2 stars', '2 STARS'),
        ('3 stars', '3 STARS'),
        ('4 stars', '4 STARS'),
        ('5 stars', '5 STARS'),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=True)