def get_prompt(requirement: str):
    return f"""
You are a QA test case generator.

Return ONLY valid JSON.

No explanation, no markdown.

Format:
{{
  "test_scenarios": [],
  "positive_test_cases": [],
  "negative_test_cases": []
}}

Requirement:
{requirement}
"""