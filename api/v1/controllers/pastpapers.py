import datetime
from typing import TYPE_CHECKING

from fastapi import File, Form, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse

from api.constants.directory import Directory
from api.core.config import SessionLocal
from api.models.models import PastPaper
from api.services.database import store_past_paper_in_db
from api.utils.upload_helpers import save_pdf_file

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def root() -> JSONResponse:
    return JSONResponse(content={"message": "/api/v1"})


async def get_all_pastpapers(request: Request) -> JSONResponse:
    db: Session = SessionLocal()
    past_papers = db.query(PastPaper).all()
    db.close()

    # Convert the past papers to a list of dictionaries
    pastpapers = [{
            "id": past_paper.id,
            "year": past_paper.year,
            "type": past_paper.type.value,  # Enum values need to be converted to their underlying value
            "session": past_paper.session.value,  # Enum values need to be converted to their underlying value
            "semester": past_paper.semester.value,  # Enum values need to be converted to their underlying value
            "date": past_paper.date.isoformat(),  # Convert the date object to a string
            "subject_id": past_paper.subject_id,
            "url": str(request.url_for("get_pastpaper_pdf", pastpaper_id= past_paper.id))  # Assuming the file is stored with this naming convention
        } for past_paper in past_papers]

    return JSONResponse(content=pastpapers)


async def get_pastpaper(request: Request, pastpaper_id: str) -> JSONResponse:
    db: Session = SessionLocal()
    past_paper = db.query(PastPaper).filter(PastPaper.id == pastpaper_id).first()
    db.close()

    if past_paper:
        pastpaper_data = {
            "id": past_paper.id,
            "year": past_paper.year,
            "type": past_paper.type.value,  # Convert Enum to its value
            "session": past_paper.session.value,  # Convert Enum to its value
            "semester": past_paper.semester.value,  # Convert Enum to its value
            "date": past_paper.date.isoformat(),  # Convert date object to ISO format
            "subject_id": past_paper.subject_id,
            "url": str(request.url_for("get_pastpaper_pdf", pastpaper_id=past_paper.id))  # URL to the past paper
        }
        return JSONResponse(content=pastpaper_data)
    return JSONResponse(status_code=404, content={"message": "Past paper not found"})



async def add_pastpaper(
    request: Request,  # noqa: ARG001
    year: int = Form(...),
    paper_type: str = Form(...),
    session: str = Form(...),
    semester: str = Form(...),
    date: str = Form(...),
    subject_id: str = Form(...),
    file: UploadFile = File(...)  # noqa: B008
) -> JSONResponse:
    db: Session = SessionLocal()

    # Convert the date string to a Python date object
    try:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # noqa: DTZ007
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")  # noqa: B904

    pastpaper_id = f"{subject_id}-{year}-{paper_type}-{session}-{semester}"
    # Save the PDF file
    pdf_file_path = Directory.PASTPAPERS_DIR / f"{pastpaper_id}.pdf"
    save_pdf_file(file, pdf_file_path)

    # Save the past paper details to the database
    past_paper_data = {
        "id": pastpaper_id,
        "year": year,
        "type": paper_type,
        "session": session,
        "semester": semester,
        "date": date_obj,
        "subject_id": subject_id
    }

    past_paper = store_past_paper_in_db(db, past_paper_data)

    db.close()

    return {
        "id": past_paper.id,
        "year": past_paper.year,
        "type": past_paper.type,
        "session": past_paper.session,
        "semester": past_paper.semester,
        "date": past_paper.date,
        "subject_id": past_paper.subject_id
    }


async def get_pastpapers_by_subject(request: Request, subject_id: str) -> JSONResponse:
    db: Session = SessionLocal()
    past_papers = db.query(PastPaper).filter(PastPaper.subject_id == subject_id).all()
    db.close()

    if past_papers:
        pastpapers_data = [{
            "id": past_paper.id,
            "year": past_paper.year,
            "type": past_paper.type.value,  # Convert Enum to its value
            "session": past_paper.session.value,  # Convert Enum to its value
            "semester": past_paper.semester.value,  # Convert Enum to its value
            "date": past_paper.date.isoformat(),  # Convert date object to ISO format
            "subject_id": past_paper.subject_id,
            "url": str(request.url_for("get_pastpaper_pdf", pastpaper_id=past_paper.id))  # URL to the past paper
        } for past_paper in past_papers]

        return JSONResponse(content=pastpapers_data)
    return JSONResponse(status_code=404, content={"message": "No past papers found for this subject"})

