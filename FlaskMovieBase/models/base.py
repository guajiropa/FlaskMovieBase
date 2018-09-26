"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates a SQLAlchemy engine to interact with our SQLite database, a SQLAlchemy 
                ORM session factory bound to that engine and a base class for our class 
                definitions to inherit from. This is the Base class that will allow all of its
                children to inherit the ORM connection to the database.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///_data/site.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()
