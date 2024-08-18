from typing import TYPE_CHECKING

from fastapi import Request
from fastapi.responses import JSONResponse

from api.core.config import SessionLocal
from api.models.models import Subject
from api.services.database import store_subject_in_db
from api.utils.request_classes import SubjectCreate

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def get_all_subjects(request: Request) -> JSONResponse:  # noqa: ARG001
    db: Session = SessionLocal()
    subjects = db.query(Subject).all()
    db.close()

    return [
        {
            "id": subject.id,
            "name": subject.name,
            "code": subject.code
        }
        for subject in subjects
    ]


async def get_subject_by_id(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_subject_by_id for {subject_id}"})


async def add_subject(request: Request, subject_create: SubjectCreate) -> JSONResponse:  # noqa: ARG001
    db: Session = SessionLocal()
    subject = store_subject_in_db(db, subject_create.dict())
    db.close()
    return {
        "id": subject.id,
        "name": subject.name,
        "code": subject.code
    }


async def update_subject(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"update_subject for {subject_id}"})


async def delete_subject(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"delete_subject for {subject_id}"})
