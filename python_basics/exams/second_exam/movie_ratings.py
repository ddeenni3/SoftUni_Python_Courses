import sys
from sys import *

movies_amount = int(input())

total_rating = 0

best_movie = None
worst_movie = None
highest_rating = -sys.maxsize
worst_rating = sys.maxsize

for i in range(movies_amount):
    movie_name = input()
    rating = float(input())
    total_rating += rating
    if rating > highest_rating:
        best_movie = movie_name
        highest_rating = rating
    elif rating < worst_rating:
        worst_movie = movie_name
        worst_rating = rating

print(f'{best_movie} is with highest rating: {highest_rating:.1f}')
print(f"{worst_movie} is with lowest rating: {worst_rating:.1f}")
print(f'Average rating: {total_rating / movies_amount:.1f}')
