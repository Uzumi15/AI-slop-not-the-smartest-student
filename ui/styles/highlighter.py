# Подсветка синтаксиса Python для отображения кода задач в GUI.


import re
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.highlighting_rules = []

        # Формат для ключевых слов
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))  # Голубой VS Code
        keyword_format.setFontWeight(QFont.Weight.Bold)

        keywords = [
            "def", "return", "if", "else", "elif", "while", "for", "in",
            "import", "from", "as", "try", "except", "raise", "abs", "round", "int", "float"
        ]
        for word in keywords:
            pattern = rf"\b{word}\b"
            self.highlighting_rules.append((re.compile(pattern), keyword_format))

        # Формат для строк
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))  # Оранжевый/Персиковый
        self.highlighting_rules.append((re.compile(r'".*?"|\'.*?\''), string_format))

        # Формат для чисел
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))  # Светло-зеленый
        self.highlighting_rules.append((re.compile(r"\b\d+(\.\d+)?\b"), number_format))

        # Формат для комментариев
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))  # Зеленый
        self.highlighting_rules.append((re.compile(r"#.*"), comment_format))

    def highlightBlock(self, text: str):
        for pattern, fmt in self.highlighting_rules:
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)