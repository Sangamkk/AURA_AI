import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import AuraMainWindow


def main():
    app = QApplication(sys.argv)

    window = AuraMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()