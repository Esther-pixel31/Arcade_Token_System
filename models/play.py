from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Play(Base):
    __tablename__ = 'plays'

    id = Column(Integer, primary_key=True)
    gamer_id = Column(Integer, ForeignKey("gamers.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    score = Column(Integer, default=0)
    played_at = Column(DateTime, default=func.now())

    # Relationships
    gamer = relationship("Gamer", back_populates="plays")
    game = relationship("Game", back_populates="plays")

    def __repr__(self):
        return f"<Play(score={self.score}, played_at={self.played_at})>"

    @classmethod
    def create(cls, session, gamer_id, game_id, score):
        play = cls(gamer_id=gamer_id, game_id=game_id, score=score)
        session.add(play)
        session.commit()
        return play

    @classmethod
    def get_all_by_gamer(cls, session, gamer_id):
        return session.query(cls).filter_by(gamer_id=gamer_id).all()

    def update_score(self, session, new_score):
        self.score = new_score
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Play {self.gamer.username} played {self.game.name} scoring {self.score}>"