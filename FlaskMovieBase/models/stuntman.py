"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates the 'Stuntman' class ORM object for the code/database interation.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.base import Base


class Stuntman(Base):
    
    __tablename__ = 'stuntmen'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    active = Column('active', Boolean)
    actor_id = Column('actor_id', Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref=backref("stuntman", uselist=False))


    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor

    def __repr__(self):
        return f'Stuntman : {self.name}.'
