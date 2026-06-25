from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from sqlalchemy.orm import Session
from models.testcase_history import TestcaseHistory


def export_to_pdf(db: Session):

    records = db.query(TestcaseHistory).all()

    pdf = SimpleDocTemplate("history.pdf")

    data = [["ID", "Requirement", "Response"]]

    for record in records:
        data.append([
            str(record.id),
            record.requirement,
            record.response
        ])

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("PADDING", (0, 0), (-1, -1), 8),
        ])
    )

    pdf.build([table])

    return {
        "message": "PDF generated successfully"
    }