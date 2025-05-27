from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Arcade Table
class Arcade(Base):
    __tablename__ = 'arcades'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    games = relationship('Game', back_populates='arcade')
    tokens = relationship('Token', back_populates='arcade')
    prizes = relationship('Prize', back_populates='arcade')

# Gamer Table
class Gamer(Base):
    __tablename__ = 'gamers'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    high_score = Column(Integer, default=0)

    tokens = relationship('Token', back_populates='gamer')
    plays = relationship('Play', back_populates='gamer')
    redemptions = relationship('Redemption', back_populates='gamer')

# Token Table
class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    points = Column(Integer)

    arcade_id = Column(Integer, ForeignKey('arcades.id'))
    gamer_id = Column(Integer, ForeignKey('gamers.id'))

    arcade = relationship('Arcade', back_populates='tokens')
    gamer = relationship('Gamer', back_populates='tokens')

# Game Table
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)

    arcade_id = Column(Integer, ForeignKey('arcades.id'))
    arcade = relationship('Arcade', back_populates='games')

    plays = relationship('Play', back_populates='game')

# Play Table (Many-to-many)
class Play(Base):
    __tablename__ = 'plays'

    id = Column(Integer, primary_key=True)
    gamer_id = Column(Integer, ForeignKey('gamers.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    score = Column(Integer, default=0)
    played_at = Column(DateTime, default=func.now())

    gamer = relationship('Gamer', back_populates='plays')
    game = relationship('Game', back_populates='plays')

# Prize Table
class Prize(Base):
    __tablename__ = 'prizes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    token_cost = Column(Integer)

    arcade_id = Column(Integer, ForeignKey('arcades.id'))
    arcade = relationship('Arcade', back_populates='prizes')

    redemptions = relationship('Redemption', back_populates='prize')

# Redemption Table (Many-to-many between Gamer and Prize)
class Redemption(Base):
    __tablename__ = 'redemptions'

    id = Column(Integer, primary_key=True)
    gamer_id = Column(Integer, ForeignKey('gamers.id'))
    prize_id = Column(Integer, ForeignKey('prizes.id'))
    redeemed_at = Column(DateTime, default=func.now())

    gamer = relationship('Gamer', back_populates='redemptions')
    prize = relationship('Prize', back_populates='redemptions')
