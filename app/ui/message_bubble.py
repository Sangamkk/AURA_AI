from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class MessageBubble(QWidget):

    def __init__(self, text, sender="ai"):
        super().__init__()
        self.sender = sender
        self.setup_ui(text)

    def setup_ui(self, text):
        layout = QVBoxLayout(self)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        if self.sender == "ai":
            self.label.setStyleSheet("""
                background:#313244;
                color:white;
                padding:12px;
                border-radius:12px;
            """)
            self.label.setAlignment(Qt.AlignLeft)
        else:
            self.label.setStyleSheet("""
                background:#89B4FA;
                color:black;
                padding:12px;
                border-radius:12px;
            """)
            self.label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.label)