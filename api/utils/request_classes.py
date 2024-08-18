from pydantic import BaseModel


class SubjectCreate(BaseModel):
    id: str
    name: str
    code: str


class UpdateSubject(BaseModel):
    id: str
    name: str
    code: str
