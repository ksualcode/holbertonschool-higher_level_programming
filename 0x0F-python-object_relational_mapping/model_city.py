#!/usr/bin/python3
''' Learning ORM '''
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    ''' City class '''

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
