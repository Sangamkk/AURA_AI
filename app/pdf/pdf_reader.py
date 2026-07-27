import fitz
from app.pdf.text_splitter import TextSplitter

class PDFReader:
    def read_pdf(self, file_path):
        document = fitz.open(file_path)
        text = ""
        for page in document:
            text += page.get_text()
        document.close()
        return text