from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from models.requirement import Requirement
from services.testcase_service import generate_testcases
from services.history_service import get_history
from services.export_service import export_to_excel
from services.search_service import search_history
from services.delete_service import delete_history
from services.clear_history_service import clear_history
from services.pdf_service import export_to_pdf

router = APIRouter()


@router.post("/generate-testcases")
def create_testcases(
    req: Requirement,
    db: Session = Depends(get_db)
):
    return generate_testcases(req.requirement, db)


@router.get("/history")
def history(
    db: Session = Depends(get_db)
):
    return get_history(db)

@router.get("/export")
def export(
    db: Session = Depends(get_db)
):
    return export_to_excel(db)

@router.get("/history/search")
def search(
    keyword: str,
    db: Session = Depends(get_db)
):
    return search_history(keyword, db)

@router.delete("/history/{history_id}")
def delete_record(
    history_id: int,
    db: Session = Depends(get_db)
):
    return delete_history(history_id, db)

@router.delete("/history")
def delete_all_history(
    db: Session = Depends(get_db)
):
    return clear_history(db)

@router.get("/pdf")
def export_pdf(
    db: Session = Depends(get_db)
):
    return export_to_pdf(db)