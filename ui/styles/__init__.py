# Это модуль управления стилями QSS и темами оформления интерфейса.


DARK_THEME_QSS = """
/* Общие настройки приложения */
QWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: 'Segoe UI', 'SF Pro Display', Roboto, Arial, sans-serif;
    font-size: 13px;
}

/* Вкладки (QTabWidget) */
QTabWidget::pane {
    border: 1px solid #2d2d2d;
    background-color: #252526;
    border-radius: 6px;
    top: -1px;
}

QTabBar::tab {
    background-color: #1e1e1e;
    color: #9cdcfe;
    padding: 10px 18px;
    margin-right: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    border: 1px solid #2d2d2d;
    border-bottom: none;
    font-weight: bold;
}

QTabBar::tab:selected {
    background-color: #252526;
    color: #4ec9b0;
    border-bottom: 2px solid #007acc;
}

QTabBar::tab:hover:!selected {
    background-color: #2a2d2e;
    color: #ffffff;
}

/* Поля ввода (QLineEdit) */
QLineEdit {
    background-color: #3c3c3c;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 6px 10px;
    color: #f8f8f2;
    selection-background-color: #264f78;
}

QLineEdit:focus {
    border: 1px solid #007acc;
    background-color: #383838;
}

/* Выпадающие списки (QComboBox) */
QComboBox {
    background-color: #3c3c3c;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 6px 10px;
    color: #ffffff;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #252526;
    border: 1px solid #3c3c3c;
    selection-background-color: #04395e;
}

/* Кнопки (QPushButton) */
QPushButton {
    background-color: #0e639c;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1177bb;
}

QPushButton:pressed {
    background-color: #094771;
}

/* Групповые контейнеры (QGroupBox) */
QGroupBox {
    border: 1px solid #3c3c3c;
    border-radius: 6px;
    margin-top: 12px;
    padding-top: 14px;
    font-weight: bold;
    color: #569cd6;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 10px;
    padding: 0 5px;
}

/* Текстовые области вывода результатов и кода (QTextEdit, QPlainTextEdit) */
QTextEdit, QPlainTextEdit {
    background-color: #141414;
    border: 1px solid #2d2d2d;
    border-radius: 4px;
    padding: 8px;
    font-family: 'Consolas', 'Fira Code', 'Courier New', monospace;
    font-size: 13px;
    color: #dcdcaa;
}

/* Прокрутка (QScrollBar) */
QScrollBar:vertical {
    border: none;
    background: #1e1e1e;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: #424242;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #4f4f4f;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""

def apply_theme(app) -> None:
    """Применяет тёмную тему ко всему приложению Qt."""
    app.setStyleSheet(DARK_THEME_QSS)