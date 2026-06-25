import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_response(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")

        # Fallback JSON
        return """
{
    "test_scenarios": [
        "Verify successful login",
        "Verify invalid password",
        "Verify empty email field",
        "Verify empty password field"
    ],
    "positive_test_cases": [
        "Login with valid credentials"
    ],
    "negative_test_cases": [
        "Login with invalid password",
        "Login with blank email"
    ],
    "expected_results": [
        "User should be logged in successfully"
    ]
}
"""