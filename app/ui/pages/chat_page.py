from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit
)
from PySide6.QtCore import QThread
from app.memory.conversation_memory import ConversationMemory
from app.ui.chat_area import ChatArea
from app.core.workers.ai_worker import AIWorker
from app.ai.prompt_builder import PromptBuilder

class ChatPage(QWidget):

    def __init__(self,pdf_manager):
        super().__init__()
        self.pdf_manager = pdf_manager
        self.memory = ConversationMemory()
        self.prompt_builder = PromptBuilder()
        self.setup_ui()
        
    def setup_input_bar(self):
        self.input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message...")
        self.message_input.setFixedHeight(40)
        self.message_input.setStyleSheet("""
            QLineEdit{
                background:#313244;
                color:white;
                border:1px solid #45475A;
                border-radius:12px;
                padding:10px;
                font-size:14px;
            }
            QLineEdit::placeholder{
                color:#9399B2;
            }
            QLineEdit:focus{
                border:2px solid #89B4FA;
            }
        """)
        self.send_button = QPushButton("Send")
        self.send_button.setFixedSize(100,40)
        self.send_button.setStyleSheet("""
            QPushButton{
                color:white;
                background:transparent;
                border:none;
                padding:14px;
                text-align:left;
                font-size:15px;
                border-radius:10px;
            }
            QPushButton:hover{
                background:#313244;
            }
            QPushButton:pressed{
                background:#45475A;
            }
        """)
        self.input_layout.addWidget(self.message_input)
        self.input_layout.addWidget(self.send_button)
        self.layout.addLayout(self.input_layout) 
        self.send_button.clicked.connect(
            self.send_message
        )
        self.message_input.returnPressed.connect(self.send_message)       
    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.chat_area = ChatArea()
        self.layout.addWidget(self.chat_area)
        self.setup_input_bar()    
        
    def generate_ai_response(self, prompt):
        self.thread = QThread()
        self.worker = AIWorker(prompt)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.display_ai_response)
        self.worker.error.connect(self.display_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()   
    def display_ai_response(self, response):
        self.chat_area.remove_thinking()
        self.chat_area.add_ai_message(response)
        self.memory.add_ai_message(response)   
        self.send_button.setEnabled(True)
        self.message_input.setEnabled(True)
        self.message_input.setFocus() 
        
    def display_error(self, error):
        self.chat_area.remove_thinking()
        self.chat_area.add_ai_message(f"❌ {error}")
        self.memory.add_ai_message(f"Error: {error}")
        self.send_button.setEnabled(True)
        self.message_input.setEnabled(True)
        self.message_input.setFocus()
      
    def build_history(self):
        history = ""
        for message in self.memory.get_history():
            history += f"{message['role']}: {message['text']}\n"
        return history      

    def build_context(self, question):
        results = self.pdf_manager.semantic_search(question)
        context = "\n\n".join(
            chunk for score, chunk in results[:5]
        )
        if not context:
            context = "No relevant document information found."
        return context
        
    def send_message(self):
        text = self.message_input.text().strip()
        if not text:
            return
        self.chat_area.add_user_message(text)
        self.message_input.clear()
        self.chat_area.show_thinking()
        context = self.build_context(text)
        self.memory.add_user_message(text)
        history = self.build_history()
        # Build prompt
        prompt = self.prompt_builder.build_chat_prompt(
            text,
            history,
            context
        )
        self.send_button.setEnabled(False)
        self.message_input.setEnabled(False)
        self.generate_ai_response(prompt)
               