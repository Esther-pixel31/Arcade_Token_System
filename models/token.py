from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
import datetime
from models import Base


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    points = Column(Integer)

    arcade_id = Column(Integer, ForeignKey("arcades.id"))
    gamer_id = Column(Integer, ForeignKey("gamers.id"))

    # Relationships
    arcade = relationship("Arcade", back_populates="tokens")
    gamer = relationship("Gamer", back_populates="tokens")

    def __repr__(self):
        return f"<Token(type='{self.type}', points={self.points})>"

    @classmethod
    def create(cls, session, type, points, arcade_id, gamer_id):
        token = cls(type=type, points=points, arcade_id=arcade_id, gamer_id=gamer_id)
        session.add(token)
        session.commit()
        return token

    @classmethod
    def get_all_for_gamer(cls, session, gamer_id):
        return session.query(cls).filter_by(gamer_id=gamer_id).all()

    def update_points(self, session, new_points):
        self.points = new_points
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def is_valid(self):
        return self.points > 0