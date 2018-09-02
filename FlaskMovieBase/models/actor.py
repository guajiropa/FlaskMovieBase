"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates the 'Actor' class ORM object for the code/database interation.
"""
from sqlalchemy import Column, String, Integer, Date
from models.base import Base

class Actor(Base):

    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    birthday = Column('birthday', Date)

 
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    
    def __repr__(self):
        return f'Actor : {self.name}'


