from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.testcase_history import TestcaseHistory


def search_history(keyword: str, db: Session):
    return db.query(TestcaseHistory).filter(
        or_(
            TestcaseHistory.requirement.ilike(f"%{keyword}%"),
            TestcaseHistory.response.ilike(f"%{keyword}%")
        )
    ).all()