from sqlalchemy.orm import Session
from models.testcase_history import TestcaseHistory


def get_history(db: Session):
    return db.query(TestcaseHistory).all()