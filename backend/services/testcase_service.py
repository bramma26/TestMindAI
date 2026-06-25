import json
from sqlalchemy.orm import Session

from services.ai_service import generate_ai_response
from services.prompt_service import get_prompt
from models.testcase_history import TestcaseHistory


def generate_testcases(requirement: str, db: Session):

    prompt = get_prompt(requirement)
    ai_output = generate_ai_response(prompt)

    # Save to database
    history = TestcaseHistory(
        requirement=requirement,
        response=ai_output
    )

    db.add(history)
    db.commit()

    try:
        parsed_output = json.loads(ai_output)

        return {
            "requirement": requirement,
            "testcases": parsed_output
        }

    except Exception as e:
        return {
            "requirement": requirement,
            "ai_response": ai_output,
            "parse_error": str(e)
        }