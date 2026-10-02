# Это главное окно приложения с объединением всех тематических категорий задач.

from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from ui.tabs import ConvertersTab, AlgebraTab, GeometryTab, BusinessTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение практических задач (1-18)")
        self.resize(1000, 700)
        self.setMinimumSize(850, 600)

        self._init_ui()

    def _init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Главный блок вкладок по категориям
        self.main_tabs = QTabWidget()

        # Добавляем тематические модули
        self.main_tabs.addTab(ConvertersTab(), " Измерения и Конвертеры")
        self.main_tabs.addTab(AlgebraTab(), " Алгебра и Уравнения")
        self.main_tabs.addTab(GeometryTab(), " Геометрия и Векторы")
        self.main_tabs.addTab(BusinessTab(), " Экономика и Бизнес")

        layout.addWidget(self.main_tabs)
        self.setCentralWidget(central_widget)