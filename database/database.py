from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///pomodoro.db")
Session = sessionmaker(engine)

def get_db_session():
    return Session
