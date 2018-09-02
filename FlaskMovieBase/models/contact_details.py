"""
AUTHOR      :   Robert James Patterson
DATE        :   08/26/2018
SYNOPSIS    :   Creates the 'ContactDetails' class ORM object for the code/database interation.
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class ContactDetails(Base):
    
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column('phone_number', String(15))
    address = Column('address', String(50))
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor



