from models.testcase_history import TestcaseHistory
from sqlalchemy.orm import Session


def clear_history(db: Session):
    db.query(TestcaseHistory).delete()
    db.commit()

    return {
        "message": "All history deleted successfully"
    }