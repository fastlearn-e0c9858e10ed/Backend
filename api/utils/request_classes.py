from typing import Literal

from pydantic import BaseModel

from api.constants.pastpapers import PaperSession, PaperType, SemesterType


class SubjectCreate(BaseModel):
    id: str
    name: str
    code: str


class UpdateSubject(BaseModel):
    id: str
    name: str
    code: str


class PastPaperCreate(BaseModel):
    id: str
    year: int
    type: Literal[PaperType.lab, PaperType.theory]
    session: Literal[PaperSession.mid1, PaperSession.mid2, PaperSession.final]
    semester: Literal[SemesterType.fall, SemesterType.spring, SemesterType.summer]
    date: str  # Use ISO 8601 date format (YYYY-MM-DD)
    subject_id: str
