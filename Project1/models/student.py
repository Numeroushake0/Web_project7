from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='SET NULL'))

    group = relationship("Group", backref="students")
    grades = relationship("Grade", back_populates="student", cascade="all, delete-orphan")
