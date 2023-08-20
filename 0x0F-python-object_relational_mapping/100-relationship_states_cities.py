#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new_state = State(name='California')
    new.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
