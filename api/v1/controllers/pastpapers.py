import datetime
from typing import TYPE_CHECKING

from fastapi import File, Form, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse

from api.constants.directory import Directory
from api.core.config import SessionLocal
from api.services.database import store_past_paper_in_db
from api.utils.upload_helpers import save_pdf_file

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


async def root() -> JSONResponse:
    return JSONResponse(content={"message": "/api/v1"})


async def get_all_pastpapers_metadata() -> JSONResponse:
    return JSONResponse(content={"message": "get_all_pastpapers"})


async def get_pastpaper_metadata(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_pastpaper_metadata for {pastpaper_id}"})


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


async def update_pastpaper(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"update_pastpaper for {pastpaper_id}"})


async def delete_pastpaper(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"delete_pastpaper for {pastpaper_id}"})


async def get_pastpapers_by_subject(subject: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_pastpapers_by_subject for {subject}"})
