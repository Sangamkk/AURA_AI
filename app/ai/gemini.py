import google.generativeai as genai

from app.core.config import Config


genai.configure(
    api_key=Config.GEMINI_API_KEY
)


class GeminiAI:

    def __init__(self):

        self.model = genai.GenerativeModel(
            Config.GEMINI_MODEL
        )

    def generate_response(self, prompt):

        response = self.model.generate_content(prompt)

        return response.text