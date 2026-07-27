from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import QTimer


class ResponseStreamer(QObject):
    updated = Signal(str)
    finished = Signal()
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.index = 0
        self.current = ""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
    def start(self):
        self.timer.start(15)

    def update_text(self):
        if self.index >= len(self.text):
            self.timer.stop()
            self.finished.emit()
            return
        self.current += self.text[self.index]
        self.index += 1
        self.updated.emit(self.current)