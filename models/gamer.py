from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Gamer(Base):
    __tablename__ = 'gamers'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    high_score = Column(Integer, default=0)

    # Relationships
    tokens = relationship("Token", back_populates="gamer")
    plays = relationship("Play", back_populates="gamer")
    redemptions = relationship("Redemption", back_populates="gamer")

    def __repr__(self):
        return f"<Gamer(username='{self.username}', high_score={self.high_score})>"

     # --- CRUD methods ---
    @classmethod
    def create(cls, session, username):
        gamer = cls(username=username)
        session.add(gamer)
        session.commit()
        return gamer

    @classmethod
    def get_by_username(cls, session, username):
        return session.query(cls).filter_by(username=username).first()

    def update_high_score(self, session, new_score):
        if new_score > self.high_score:
            self.high_score = new_score
            session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

        
    def total_tokens(self):
        return sum(token.points for token in self.tokens)

    def redeem_prize(self, session, prize):
        if self.total_tokens() >= prize.token_cost:
            redemption = Redemption(gamer_id=self.id, prize_id=prize.id)
            session.add(redemption)
            session.commit()
            return redemption
        else:
            raise ValueError("Not enough tokens to redeem this prize.")

    def play_game(self, session, game, score=0):
        from .play import Play
        play = Play(gamer_id=self.id, game_id=game.id, score=score)
        session.add(play)
        if score > self.high_score:
            self.high_score = score
        session.commit()
        return play


    

