from sqlalchemy.orm import Session

from api.models.models import Subject


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
