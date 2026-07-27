from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QFrame
)
from app.ui.message_bubble import MessageBubble
from PySide6.QtCore import QTimer

class ChatArea(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setFrameShape(QFrame.NoFrame)
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_scroll.setWidget(self.chat_container)
        self.main_layout.addWidget(self.chat_scroll)
        self.add_ai_message(
            "👋 Hello!\n\nI'm Aura AI.\nHow can I help you today?"
        )

    def add_ai_message(self, text):
        bubble = MessageBubble(text, "ai")
        self.chat_layout.addWidget(bubble)
        QTimer.singleShot(0, self.scroll_to_bottom)
    def add_user_message(self, text):
        bubble = MessageBubble(text, "user")
        self.chat_layout.addWidget(bubble)
        QTimer.singleShot(0, self.scroll_to_bottom)
    
    def scroll_to_bottom(self):
        scrollbar = self.chat_scroll.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())     
        
    def show_thinking(self):
        self.thinking_bubble = MessageBubble(
            "🤖 Thinking...",
            "ai"
        )
        self.chat_layout.addWidget(self.thinking_bubble)
        QTimer.singleShot(0, self.scroll_to_bottom)    
    
    def remove_thinking(self):
        if hasattr(self, "thinking_bubble"):
            self.chat_layout.removeWidget(self.thinking_bubble)
            self.thinking_bubble.deleteLater()
            self.thinking_bubble = None    
            
    def create_ai_bubble(self):
        bubble = MessageBubble("", "ai")
        self.chat_layout.addWidget(bubble)
        return bubble        