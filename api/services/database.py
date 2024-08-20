from sqlalchemy.orm import Session

from api.models.models import PastPaper, Subject


def store_subject_in_db(db: Session, subject: dict) -> Subject:
    db_subject = db.query(Subject).filter(Subject.id == subject["id"]).first()
    if not db_subject:
        db_subject = Subject(
            id=subject["id"],
            name=subject["name"],
            code=subject["code"]
        )
        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)
    return db_subject


def store_past_paper_in_db(db: Session, past_paper: dict) -> PastPaper:
    db_past_paper = db.query(PastPaper).filter(PastPaper.id == past_paper["id"]).first()
    if not db_past_paper:
        db_past_paper = PastPaper(
            id=past_paper["id"],
            year=past_paper["year"],
            type=past_paper["type"],
            session=past_paper["session"],
            semester=past_paper["semester"],
            date=past_paper["date"],
            subject_id=past_paper["subject_id"]
        )
        db.add(db_past_paper)
        db.commit()
        db.refresh(db_past_paper)
    return db_past_paper
