from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QFileDialog,
    QMessageBox
)
from app.pdf.chunk_search import ChunkSearcher
from app.pdf.pdf_manager import PDFManager

class PDFPage(QWidget):

    def __init__(self,pdf_manager):
        super().__init__()
        self.manager = pdf_manager
        self.searcher = ChunkSearcher()
        self.setup_ui()
        
    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        title = QLabel("📄 Document Library")
        self.layout.addWidget(title)
        self.pdf_list = QListWidget()
        self.layout.addWidget(self.pdf_list)
        self.add_button = QPushButton("Add PDF")
        self.remove_button = QPushButton("Remove Selected")
        self.clear_button = QPushButton("Clear Library")
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.clear_button)  
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#2E3440;
        """) 
        button_style = """
        QPushButton{
            background-color:#1E1E2E;
            color:white;
            border:none;
            border-radius:10px;
            padding:10px;
            font-size:14px;
        }

        QPushButton:hover{
            background:#74C7EC;
        }

        QPushButton:pressed{
            background:#5DADE2;
        }
        """

        self.add_button.setStyleSheet(button_style)
        self.remove_button.setStyleSheet(button_style)
        self.clear_button.setStyleSheet(button_style)
        self.add_button.clicked.connect(self.add_pdf)
        self.remove_button.clicked.connect(self.remove_pdf)
        self.clear_button.clicked.connect(self.clear_library)
        self.pdf_list.setStyleSheet("""
        QListWidget{
            background:white;
            border:1px solid #C0C0C0;
            border-radius:10px;
            color:black;
            font-size:14px;
            padding:5px;
        }
        """) 
        
    def add_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF",
            "",
            "PDF Files (*.pdf)"
        )
        if not file_path:
            return
        document = self.manager.load_document(file_path)
        results = self.searcher.search(
            document.chunks,
            "java"
        )
        print(results)
        print(f"Total Chunks: {len(document.chunks)}")
        for i, chunk in enumerate(document.chunks):
            print(f"\nChunk {i+1}")
            print(chunk[:150])
        self.refresh_list()

    def remove_pdf(self):
        current_item = self.pdf_list.currentItem()
        if current_item is None:
            QMessageBox.information(
                self,
                "No Selection",
                "Please select a PDF first."
            )
            return
        filename = current_item.text()
        for document in self.manager.get_documents():
            if document.name == filename:
                self.manager.remove_document(document)
                break
        self.refresh_list()


    def clear_library(self):
        reply = QMessageBox.question(
            self,
            "Clear Library",
            "Remove all PDFs?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.manager.clear_documents()
            self.refresh_list()    

    def refresh_list(self):
        self.pdf_list.clear()
        for document in self.manager.get_documents():
            self.pdf_list.addItem(document.name)