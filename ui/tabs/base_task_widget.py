# И так это базовый виджет карточки для одной задачи.
# Автоматически строит UI по конфигурации:
# 1) Заголовок и условие задачи
# 2) Поля ввода аргументов
# 3) Кнопку выполнения
# 4) Вывод результата
# 5) Окно просмотра исходного кода с подсветкой синтаксиса Python

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QTextEdit, QGroupBox, QSplitter, QTabWidget
)
from PySide6.QtCore import Qt
from ui.styles.highlighter import PythonSyntaxHighlighter
from utils.validators import parse_float, parse_int

class TaskCardWidget(QWidget):
    def __init__(self, task_num: int, title: str, description: str, fields: list[tuple[str, str, type]], solve_func, code_str: str, format_result_func=None):
        super().__init__()
        self.task_num = task_num
        self.solve_func = solve_func
        self.fields_config = fields  # Список кортежей: [("var_name", "Метка поля", float/int)]
        self.code_str = code_str
        self.format_result_func = format_result_func
        self.input_fields = {}

        self._init_ui(title, description)

    def _init_ui(self, title: str, description: str):
        main_layout = QVBoxLayout(self)

        # Главный разделитель: слева интерактивная форма, справа — исходный код
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # --- Левая панель: Решение задачи ---
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        # Описание задачи
        desc_group = QGroupBox(f"Задача №{self.task_num}: {title}")
        desc_layout = QVBoxLayout()
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_layout.addWidget(desc_label)
        desc_group.setLayout(desc_layout)
        left_layout.addWidget(desc_group)

        # Поля ввода
        inputs_group = QGroupBox("Входные данные")
        inputs_layout = QVBoxLayout()
        for var_name, label_text, _ in self.fields_config:
            row = QHBoxLayout()
            lbl = QLabel(f"{label_text}:")
            lbl.setMinimumWidth(140)
            inp = QLineEdit()
            inp.setPlaceholderText("Введите значение...")
            self.input_fields[var_name] = inp
            row.addWidget(lbl)
            row.addWidget(inp)
            inputs_layout.addLayout(row)
        inputs_group.setLayout(inputs_layout)
        left_layout.addWidget(inputs_group)

        # Кнопка расчета
        self.btn_calc = QPushButton(" Вычислить")
        self.btn_calc.setMinimumHeight(36)
        self.btn_calc.clicked.connect(self._on_calculate)
        left_layout.addWidget(self.btn_calc)

        # Вывод результата
        res_group = QGroupBox("Результат выполнения")
        res_layout = QVBoxLayout()
        self.res_display = QTextEdit()
        self.res_display.setReadOnly(True)
        self.res_display.setMaximumHeight(100)
        res_layout.addWidget(self.res_display)
        res_group.setLayout(res_layout)
        left_layout.addWidget(res_group)

        left_layout.addStretch()

        # --- Правая панель: Код программы ---
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        code_group = QGroupBox("Исходный код алгоритма")
        code_layout = QVBoxLayout()

        self.code_display = QTextEdit()
        self.code_display.setReadOnly(True)
        self.code_display.setPlainText(self.code_str)
        # Подключаем подсветку синтаксиса
        self.highlighter = PythonSyntaxHighlighter(self.code_display.document())

        code_layout.addWidget(self.code_display)
        code_group.setLayout(code_layout)
        right_layout.addWidget(code_group)

        # Добавляем левую и правую части в Splitter
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([450, 450])

        main_layout.addWidget(splitter)

    def _on_calculate(self):
        try:
            kwargs = {}
            for var_name, label_text, data_type in self.fields_config:
                raw_val = self.input_fields[var_name].text()
                if data_type == int:
                    kwargs[var_name] = parse_int(raw_val, label_text)
                else:
                    kwargs[var_name] = parse_float(raw_val, label_text)

            res = self.solve_func(**kwargs)

            if self.format_result_func:
                if isinstance(res, tuple):
                    res_text = self.format_result_func(*res)
                else:
                    res_text = self.format_result_func(res)
            else:
                res_text = str(res)

            self.res_display.setHtml(f"<b style='color: #4EC9B0;'>Результат:</b> {res_text}")
        except Exception as e:
            self.res_display.setHtml(f"<b style='color: #F14C4C;'>Ошибка:</b> {str(e)}")