# db/engine.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///arcade.db")
Session = sessionmaker(bind=engine)
