"""
AUTHOR      :   Robert James Patterson
DATE        :   09/24/2018
SYNOPSIS    :   This script runs the application using a development server. It contains the 
                definition of routes and views for the application, the main which loads the 
                'Flask' server and the glue to all of the other modules in this application.
"""
from datetime import date
from models.actor import Actor
from models.movie import Movie
from models.stuntman import Stuntman
from models.contact_details import ContactDetails
from models.base import Base, Session, engine
from flask import Flask, redirect, render_template, request, url_for
 

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/listing')
def listing():
    # Create a session.
    session = Session()

    # Get all movies.
    movies = session.query(Movie).all()

    # Render the 'listing' template and pass it the 'movies' list
    return render_template('listing.html', movies=movies)


@app.route('/comments')
def comments():
    pass


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
