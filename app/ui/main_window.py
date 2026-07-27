from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QLabel,
    QLineEdit
)
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import Qt,QThread
from app.core.workers.ai_worker import AIWorker
from app.ui.chat_area import ChatArea

from app.ui.pages.chat_page import ChatPage
from app.ui.pages.pdf_page import PDFPage
from app.ui.pages.ocr_page import OCRPage
from app.ui.pages.voice_page import VoicePage
from app.ui.pages.memory_page import MemoryPage
from app.ui.pages.settings_page import SettingsPage
from app.pdf.pdf_manager import PDFManager

class AuraMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.pdf_manager = PDFManager()
        self.setup_main_layout()
        self.setup_sidebar()
        self.setup_content()
        
    def setup_window(self):
        self.setWindowTitle("AURA AI")
        self.resize(1200, 700)
        self.setMinimumSize(900, 600)
        self.center_window()  
    
    def setup_main_layout(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(250)

        self.content = QFrame()

        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)  
    def setup_sidebar(self):
        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)
        self.logo = QLabel("AURA AI")
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("""
            color:white;
            font-size:22px;
            font-weight:bold;
            padding:20px;
        """)
        self.sidebar_layout.addWidget(self.logo)

        menu_items = [
            "💬 Chat",
            "📄 PDF Chat",
            "🖼 OCR",
            "📂 Files",
            "🎤 Voice",
            "🧠 Memory",
            "⚙ Settings"
        ]
        self.buttons = []
        for item in menu_items:
            button = QPushButton(item)
            self.buttons.append(button)
            button.setStyleSheet("""
                QPushButton{
                    color:white;
                    background:transparent;
                    border:none;
                    padding:12px;
                    text-align:left;
                    font-size:15px;
                }

                QPushButton:hover{
                    background:#434C5E;
                    border-radius:8px;
                }
            """)

            self.sidebar_layout.addWidget(button)

        self.sidebar_layout.addStretch()
        for index, button in enumerate(self.buttons):
            if index < 6:
                button.clicked.connect(
                    lambda checked, i=index: self.stack.setCurrentIndex(i)
                )
        self.sidebar.setStyleSheet("""
            background-color:#181825;
        """) 
    def setup_content(self):
        self.content_layout = QVBoxLayout()
        self.content.setLayout(self.content_layout)
        self.stack = QStackedWidget()

        self.chat_page = ChatPage(self.pdf_manager)
        self.pdf_page = PDFPage(self.pdf_manager)
        self.ocr_page = OCRPage()
        self.voice_page = VoicePage()
        self.memory_page = MemoryPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.chat_page)
        self.stack.addWidget(self.pdf_page)
        self.stack.addWidget(self.ocr_page)
        self.stack.addWidget(self.voice_page)
        self.stack.addWidget(self.memory_page)
        self.stack.addWidget(self.settings_page)

        self.content_layout.addWidget(self.stack)
        self.content.setStyleSheet("""
            background-color:#ECEFF4;
        """) 
            
    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())

        self.move(window_geometry.topLeft())
      
        