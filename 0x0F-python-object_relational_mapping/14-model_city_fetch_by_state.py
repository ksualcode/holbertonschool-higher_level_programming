#!/usr/bin/python3
''' Prints the first state '''
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    for row in session.query(City, State).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(row[1].name, row[0].id, row[0].name))
    session.close()
