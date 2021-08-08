#!/usr/bin/python3
''' Prints a state with an "a" on it '''
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        if ('a' in state.name):
            print("{}: {}".format(state.id, state.name))
    session.close()
