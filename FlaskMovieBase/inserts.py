"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates the [/_data/site.db] file. Create the movies, actors, stuntmen and the 
                contact_details tables with some filler starter data.
"""
from datetime import date
from models.actor import Actor
from models.movie import Movie
from models.stuntman import Stuntman
from models.contact_details import ContactDetails
from models.base import Base, Session, engine

# Generate the database schema.
Base.metadata.create_all(engine)

# Create a new session.
session = Session()

# Create metadata for Movies.
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_seven = Movie("Furious 7", date(2015, 4, 2))
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

# Create metadata for Actors
matt_damon = Actor("Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

# Add Actors to Movies.
bourne_identity.actors = [matt_damon]
furious_seven.actors = [dwayne_johnson]
pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]

# Add contact details for actors.
matt_contact = ContactDetails("818 525 6850", "Burbank, CA", matt_damon)
dwayne_contact = ContactDetails("818 555 5623", "Glendale, CA", dwayne_johnson)
dwayne_contact_2 = ContactDetails("232 555 7679", "Wasr Hollywood, CA", dwayne_johnson)
mark_contact = ContactDetails("818 765 8359", "Glendale, CA", mark_wahlberg)

# Create the stuntmen.
matt_stuntman = Stuntman("Joe Mama", True, matt_damon)
dwayne_stuntman = Stuntman("Joe Dirt", True, dwayne_johnson)
mark_stuntman = Stuntman("Richard Roe", True, mark_wahlberg)

# Persist the data
session.add(bourne_identity)
session.add(furious_seven)
session.add(pain_and_gain)

session.add(matt_contact)
session.add(dwayne_contact)
session.add(dwayne_contact_2)
session.add(mark_contact)

session.add(mark_stuntman)
session.add(dwayne_contact)
session.add(mark_stuntman)

# Commit data to the database and close the session
session.commit()
session.close()
