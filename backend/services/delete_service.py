from sqlalchemy.orm import Session
from models.testcase_history import TestcaseHistory


def delete_history(history_id: int, db: Session):
    record = db.query(TestcaseHistory).filter(
        TestcaseHistory.id == history_id
    ).first()

    if not record:
        return {
            "message": "Record not found"
        }

    db.delete(record)
    db.commit()

    return {
        "message": f"Record {history_id} deleted successfully"
    }