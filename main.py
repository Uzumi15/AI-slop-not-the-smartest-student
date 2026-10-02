# И наконец-то точка входа в графическое приложение (PySide6).

import sys
from PySide6.QtWidgets import QApplication
from ui import MainWindow
from ui.styles import apply_theme

def main():
    app = QApplication(sys.argv)
    
    # Применяем стили тёмной темы
    apply_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()