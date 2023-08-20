#!/usr/bin/python3
"""prints all City objects
from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":

    import sys

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
