from typing import TYPE_CHECKING

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from api.core.config import SessionLocal
from api.models.models import Subject
from api.services.database import store_subject_in_db
from api.utils.request_classes import SubjectCreate, UpdateSubject

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


async def get_subject_by_id(request: Request, subject_id: str) -> JSONResponse:  # noqa: ARG001
    db: Session = SessionLocal()
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    db.close()

    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    return {
        "id": subject.id,
        "name": subject.name,
        "code": subject.code
    }


async def add_subject(request: Request, subject_create: SubjectCreate) -> JSONResponse:  # noqa: ARG001
    db: Session = SessionLocal()
    subject = store_subject_in_db(db, subject_create.dict())
    db.close()
    return {
        "id": subject.id,
        "name": subject.name,
        "code": subject.code
    }


async def update_subject(request: Request, subject_id: str, update_subject: UpdateSubject) -> JSONResponse:  # noqa: ARG001
    db: Session = SessionLocal()

    # Find the subject to update
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if subject is None:
        db.close()
        raise HTTPException(status_code=404, detail="Subject not found")

    # Check if the new ID already exists
    if update_subject.id != subject_id:
        existing_subject = db.query(Subject).filter(Subject.id == update_subject.id).first()
        if existing_subject:
            db.close()
            raise HTTPException(status_code=400, detail="New subject ID already exists")

    # Update the subject's details
    subject.id = update_subject.id
    subject.name = update_subject.name
    subject.code = update_subject.code

    db.commit()
    db.refresh(subject)
    db.close()

    return {
        "id": subject.id,
        "name": subject.name,
        "code": subject.code
    }


async def delete_subject(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"delete_subject for {subject_id}"})
