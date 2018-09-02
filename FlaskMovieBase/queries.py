"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Query the movies database using the ORM objects and the Query API.
"""
from datetime import date
from models.actor import Actor
from models.movie import Movie
from models.stuntman import Stuntman
from models.contact_details import ContactDetails
from models.base import Session

# Create a session.
session = Session()

# Get all movies.
movies = session.query(Movie).all()

print('\n### All Movies:\n')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# Get all movie after 01-01-15.
movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()

print('### Recent Movies\n')
for movie in movies:
    print(f'{movie.title} was released after 01/01/2015.')
print('')

# Get movies that Dwayne Johnson stared in.
rock_movies = session.query(Movie).join(Actor, Movie.actors) \
               .filter(Actor.name == 'Dwayne Johnson').all()

print('### Dwayne Johnson movies\n')
for movie in rock_movies:
    print(f'The Rock stared in {movie.title}.')
print('')

# Get actors that have a house in Glendale.
glendale_stars = session.query(Actor).join(ContactDetails) \
                    .filter(ContactDetails.address.ilike('%glendale%')).all()

print('### Actors who have homes in Glendale\n')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale.')
print('')