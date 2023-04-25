#!/usr/bin/python3
"""
    This is a Script that prints all City objects
    from the database hbtn_0e_14_usa sorted by cities.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 4:
        print('Usage: ./14-model_city_fetch_by_state.py <mysql_username> \
                                                      <mysql_password> \
                                                      <database_name>')
        sys.exit(1)

    # Create the connection string to the database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all cities and their respective states and sort them by city id
    cities = session.query(City, State.name)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id)\
                    .all()

    # Print the result in the required format
    for city, state_name in cities:
        print(f'{state_name}: ({city.id}) {city.name}')
