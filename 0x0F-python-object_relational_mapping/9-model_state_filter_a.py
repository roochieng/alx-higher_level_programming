#!/usr/bin/python3
"""A script that lists all State
objects that contains the letter a
 from the database hbtn_0e_6_usa"""


if __name__ == '__main__':

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id):
        print(f"{state.id}: {state.name}")
    session.close()
