from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Arcade(Base):
    __tablename__ = 'arcades'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    # Relationships
    tokens = relationship("Token", back_populates="arcade")
    games = relationship("Game", back_populates="arcade")
    prizes = relationship("Prize", back_populates="arcade")

    def __repr__(self):
        return f"<Arcade(name='{self.name}', location='{self.location}')>"

    # --- CRUD methods ---

    @classmethod
    def create(cls, session, name, location):
        arcade = cls(name=name, location=location)
        session.add(arcade)
        session.commit()
        return arcade

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, arcade_id):
        return session.query(cls).filter_by(id=arcade_id).first()

    def update_location(self, session, new_location):
        self.location = new_location
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def available_prizes(self):
        return self.prizes

    def distribute_token(self, gamer, type, points):
        from .token import Token
        token = Token(type=type, points=points, arcade_id=self.id, gamer_id=gamer.id)
        return token

    def top_gamers(self, limit=5):
        gamers = sorted(
            {token.gamer for token in self.tokens},
            key=lambda g: g.high_score,
            reverse=True
        )
        return gamers[:limit]