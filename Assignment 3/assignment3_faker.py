# Elise May
# Student ID: 2271041
# Email: may137@mail.chapman.edu
# CPSC 408
# Assignment 3

import csv
from faker import Faker

fake = Faker()

# Generate mood options
mood_list = ["sad", "happy", "romantic", "scary", "thrilling", "inspiring"]

# Generate genre options
genre_list = ["action", "comedy", "romance", "horror", "documentary", "family"]

# Get user input for file name & # of tuples
file_name = input("File name: ")
print("CSV File Name - " + file_name)

num_tup = int(input("Number of tuples to generate: "))
print("# of Tuples - ", num_tup)

# Append file type
file = file_name + ".csv"

# Create file & file writer
csv_file = open(file, 'w')
writer = csv.writer(csv_file)

# Write to file, insert table name as first entry for each row (used for importing)
for x in range(0, num_tup):
    # MovieInfo(movieID, title, genre, director, length, actors (3), mood, rating)
    writer.writerow(["1",
                     x,
                     fake.text(max_nb_chars=20),
                     fake.word(ext_word_list=genre_list),
                     fake.name(),
                     fake.time(),
                     fake.name(),
                     fake.name(),
                     fake.name(),
                     fake.word(ext_word_list=mood_list),
                     fake.pydecimal(right_digits=1, min_value=0, max_value=5)])

    # UserInfo(userID, first, last)
    writer.writerow(["2",
                     x,
                     fake.first_name(),
                     fake.last_name()])

    # UserRating(movieID FK, userID FK, rating, userMood)
    writer.writerow(["3",
                     fake.pyint(min_value=1, max_value=num_tup),
                     fake.pyint(min_value=1, max_value=num_tup),
                     fake.pydecimal(right_digits=1, min_value=0, max_value=5),
                     fake.word(ext_word_list=mood_list)])

    # WantToWatch(userID FK, movieID FK)
    writer.writerow(["4",
                     fake.pyint(min_value=1, max_value=num_tup),
                     fake.pyint(min_value=1, max_value=num_tup)])

    # UserWatched(userID FK, movieID FK)
    writer.writerow(["5",
                     fake.pyint(min_value=1, max_value=num_tup),
                     fake.pyint(min_value=1, max_value=num_tup)])
