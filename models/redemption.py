from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Redemption(Base):
    __tablename__ = 'redemptions'

    id = Column(Integer, primary_key=True)
    gamer_id = Column(Integer, ForeignKey("gamers.id"))
    prize_id = Column(Integer, ForeignKey("prizes.id"))
    redeemed_at = Column(DateTime, default=func.now())

    # Relationships
    gamer = relationship("Gamer", back_populates="redemptions")
    prize = relationship("Prize", back_populates="redemptions")

    def __repr__(self):
        return f"<Redemption(redeemed_at={self.redeemed_at})>"
    
    @classmethod
    def create(cls, session, gamer_id, prize_id):
        redemption = cls(gamer_id=gamer_id, prize_id=prize_id)
        session.add(redemption)
        session.commit()
        return redemption

    @classmethod
    def get_all_by_gamer(cls, session, gamer_id):
        return session.query(cls).filter_by(gamer_id=gamer_id).all()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Redemption: {self.gamer.username} redeemed {self.prize.name} on {self.redeemed_at}>"