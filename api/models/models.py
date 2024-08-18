from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from api.constants.pastpapers import PaperSession, PaperType, SemesterType

Base = declarative_base()

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)

    # Relationship with PastPapers
    past_papers = relationship("PastPaper", back_populates="subject")


class PastPaper(Base):
    __tablename__ = "past_papers"

    id = Column(String, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    type = Column(Enum(PaperType), nullable=False)
    session = Column(Enum(PaperSession), nullable=False)
    semester = Column(Enum(SemesterType), nullable=False)
    date = Column(Date, nullable=False)

    # Foreign key to Subject
    subject_id = Column(String, ForeignKey("subjects.id"))

    # Relationship with Subject
    subject = relationship("Subject", back_populates="past_papers")
