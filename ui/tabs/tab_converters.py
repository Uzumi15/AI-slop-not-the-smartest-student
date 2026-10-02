# Это вкладка конвертеров и систем измерения (Задачи 1, 2, 3, 4, 10).

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.tabs.base_task_widget import TaskCardWidget
from logic import task_01, task_02, task_03, task_04, task_10
from utils.converters import format_angle_dms, format_time_hms, format_russian_length

class ConvertersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        sub_tabs = QTabWidget()

        # Задача 1
        t1 = TaskCardWidget(
            task_num=1,
            title="Угол из ГМС в радианы",
            description="Задан угол в градусах, минутах и секундах. Найти его величину в радианах с максимальной точностью (работает для углов > 180° и отрицательных).",
            fields=[("deg", "Градусы", float), ("minutes", "Минуты", float), ("seconds", "Секунды", float)],
            solve_func=task_01.solve,
            code_str=task_01.TASK_CODE,
            format_result_func=lambda rad: f"{rad:.10f} рад"
        )

        # Задача 2
        t2 = TaskCardWidget(
            task_num=2,
            title="Угол из радиан в ГМС",
            description="Задан угол в радианах. Перевести в градусы, минуты и секунды.",
            fields=[("rad", "Радианы", float)],
            solve_func=task_02.solve,
            code_str=task_02.TASK_CODE,
            format_result_func=format_angle_dms
        )

        # Задача 3
        t3 = TaskCardWidget(
            task_num=3,
            title="Дюймы в метрическую систему",
            description="Перевод длины отрезка из дюймов в метры, сантиметры и миллиметры.",
            fields=[("inches", "Длина (дюймы)", float)],
            solve_func=task_03.solve,
            code_str=task_03.TASK_CODE,
            format_result_func=lambda m, cm, mm: f"{m} м {cm} см {mm:.2f} мм"
        )

        # Задача 4
        t4 = TaskCardWidget(
            task_num=4,
            title="Продолжительность интервала времени",
            description="Заданы моменты начала и конца промежутка времени в пределах суток. Найти его продолжительность.",
            fields=[
                ("h1", "Час начала", int), ("m1", "Мин начала", int), ("s1", "Сек начала", int),
                ("h2", "Час конца", int), ("m2", "Мин конца", int), ("s2", "Сек конца", int)
            ],
            solve_func=task_04.solve,
            code_str=task_04.TASK_CODE,
            format_result_func=format_time_hms
        )

        # Задача 10
        t10 = TaskCardWidget(
            task_num=10,
            title="Русские неметрические единицы",
            description="Перевод отрезка в метрах в версты, сажени, аршины и вершки.",
            fields=[("meters", "Длина (метры)", float)],
            solve_func=task_10.solve,
            code_str=task_10.TASK_CODE,
            format_result_func=format_russian_length
        )

        sub_tabs.addTab(t1, "Зад. 1 (ГМС -> Рад)")
        sub_tabs.addTab(t2, "Зад. 2 (Рад -> ГМС)")
        sub_tabs.addTab(t3, "Зад. 3 (Дюймы)")
        sub_tabs.addTab(t4, "Зад. 4 (Время)")
        sub_tabs.addTab(t10, "Зад. 10 (Рус. единицы)")

        layout.addWidget(sub_tabs)