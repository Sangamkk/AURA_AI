import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    # ==========================
    # Gemini
    # ==========================
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash"
    # ==========================
    # PDF
    # ==========================
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    MAX_CONTEXT_CHUNKS = 5
    # ==========================
    # Chat
    # ==========================
    MAX_HISTORY = 20
    # ==========================
    # UI
    # ==========================
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 700