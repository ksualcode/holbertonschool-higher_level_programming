#!/usr/bin/python3
''' Prints the first state '''
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
    boolean = False
    for state in session.query(State).order_by(State.id).all():
        if (argv[4] == state.name):
            boolean = True
            print("{}: {}".format(state.id, state.name))
    if (not boolean):
        print("Not found")
    session.close()
