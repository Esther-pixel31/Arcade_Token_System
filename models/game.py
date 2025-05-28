from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    arcade_id = Column(Integer, ForeignKey("arcades.id"))

    # Relationships
    arcade = relationship("Arcade", back_populates="games")
    plays = relationship("Play", back_populates="game")

    def __repr__(self):
        return f"<Game(name='{self.name}', genre='{self.genre}')>"
    
    @classmethod
    def create(cls, session, name, genre, arcade_id):
        game = cls(name=name, genre=genre, arcade_id=arcade_id)
        session.add(game)
        session.commit()
        return game

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, game_id):
        return session.query(cls).filter_by(id=game_id).first()

    def update_genre(self, session, new_genre):
        self.genre = new_genre
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()