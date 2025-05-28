from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Prize(Base):
    __tablename__ = 'prizes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    token_cost = Column(Integer)
    arcade_id = Column(Integer, ForeignKey("arcades.id"))

    # Relationships
    arcade = relationship("Arcade", back_populates="prizes")
    redemptions = relationship("Redemption", back_populates="prize")

    def __repr__(self):
        return f"<Prize(name='{self.name}', token_cost={self.token_cost})>"

    @classmethod
    def create(cls, session, name, token_cost, arcade_id):
        prize = cls(name=name, token_cost=token_cost, arcade_id=arcade_id)
        session.add(prize)
        session.commit()
        return prize

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def update_token_cost(self, session, new_cost):
        self.token_cost = new_cost
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def can_be_redeemed_by(self, gamer):
        return gamer.total_tokens() >= self.token_cost