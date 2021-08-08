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
    first = session.query(State).order_by(State.id).first()
    if (first):
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
