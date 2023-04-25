#!/usr/bin/python3
"""
    This is one lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # dialect+driver://username:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    # create all the objects that inherit from Base
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session instance
    session = Session()

    # query all State objects that contain the letter a
    states = session.query(State)
    .filter(State.name.like('%a%'))
    .order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    session.close()
