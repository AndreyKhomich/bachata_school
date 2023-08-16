from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    tg_first_name = Column(String(250))
    tg_last_name = Column(String(250))
    phone_number = Column(String(20), unique=True)
    age = Column(String(10))
    status = Column(String(25))

    subscriptions = relationship("Subscription", back_populates="user")


class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True, index=True)
    visited_classes = Column(Integer)
    classes = Column(Integer)
    remaining_classes = Column(Integer)
    date = Column(Date())
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="subscriptions")
