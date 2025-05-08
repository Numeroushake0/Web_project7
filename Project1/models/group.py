from sqlalchemy import Column, Integer, String
from .base import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
