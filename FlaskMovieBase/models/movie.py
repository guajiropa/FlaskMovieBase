"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates the 'Movie' class ORM object for the code/database interation and the 
                    'movie_actors' link table.
"""
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

movies_actors_association = Table(
    'movie_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
    )

class Movie(Base):
    
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column('title', String(75))
    release_date = Column('release_date', Date)
    actors = relationship("Actor", secondary=movies_actors_association)
   
    
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


    def __repr__(self):
        return f'Movie : {self.title}'


