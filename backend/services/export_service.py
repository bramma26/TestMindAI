from openpyxl import Workbook
from sqlalchemy.orm import Session
from models.testcase_history import TestcaseHistory


def export_to_excel(db: Session):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "History"

    # Header
    sheet.append(["ID", "Requirement", "Response"])

    # Fetch records
    history = db.query(TestcaseHistory).all()

    for row in history:
        sheet.append([
            row.id,
            row.requirement,
            row.response
        ])

    workbook.save("history.xlsx")

    return {
        "message": "Excel file generated successfully",
        "filename": "history.xlsx"
    }