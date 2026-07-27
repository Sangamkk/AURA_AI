from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot

from app.ai.gemini import GeminiAI


class AIWorker(QObject):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt
        self.ai = GeminiAI()
    @Slot()
    def run(self):
        try:
            response = self.ai.generate_response(
                self.prompt
            )
            self.finished.emit(response)
        except Exception as e:
            self.error.emit(str(e))