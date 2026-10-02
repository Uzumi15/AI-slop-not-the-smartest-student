# Это вкладка геометрии и векторов (Задачи 9, 11, 14, 15, 17).

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.tabs.base_task_widget import TaskCardWidget
from logic import task_09, task_11, task_14, task_15, task_17

class GeometryTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        sub_tabs = QTabWidget()

        # Задача 9
        t9 = TaskCardWidget(
            task_num=9,
            title="Угол между двумя прямыми",
            description="Нахождение угла (в градусах и минутах) между y = k₁x + b₁ и y = k₂x + b₂.",
            fields=[("k1", "Угловой коэф. k1", float), ("k2", "Угловой коэф. k2", float)],
            solve_func=task_09.solve,
            code_str=task_09.TASK_CODE,
            format_result_func=lambda deg, min_: f"Угол между прямыми: {deg}° {min_}'"
        )

        # Задача 11
        t11 = TaskCardWidget(
            task_num=11,
            title="Равнобедренный прямоугольный треугольник",
            description="Нахождение сторон по известной высоте h, опущенной на гипотенузу.",
            fields=[("h", "Высота h", float)],
            solve_func=task_11.solve,
            code_str=task_11.TASK_CODE,
            format_result_func=lambda a, b, c: f"Катет a = {a}, Катет b = {b}, Гипотенуза c = {c}"
        )

        # Задача 14
        t14 = TaskCardWidget(
            task_num=14,
            title="Внутренние углы треугольника",
            description="Расчет внутренних углов треугольника по координатам его вершин A, B, C.",
            fields=[
                ("x1", "Ax", float), ("y1", "Ay", float),
                ("x2", "Bx", float), ("y2", "By", float),
                ("x3", "Cx", float), ("y3", "Cy", float)
            ],
            solve_func=task_14.solve,
            code_str=task_14.TASK_CODE,
            format_result_func=lambda A, B, C: f"Угол A: {A}°, Угол B: {B}°, Угол C: {C}°"
        )

        # Задача 15
        t15 = TaskCardWidget(
            task_num=15,
            title="Угол между 3D векторами",
            description="Нахождение угла в градусах между векторами A(xa, ya, za) и B(xb, yb, zb).",
            fields=[
                ("xa", "Xa", float), ("ya", "Ya", float), ("za", "Za", float),
                ("xb", "Xb", float), ("yb", "Yb", float), ("zb", "Zb", float)
            ],
            solve_func=task_15.solve,
            code_str=task_15.TASK_CODE,
            format_result_func=lambda angle: f"Угол между векторами: {angle}°"
        )

        # Задача 17
        t17 = TaskCardWidget(
            task_num=17,
            title="Вершины квадрата",
            description="По противоположным вершинам квадрата A и C найти координаты B и D.",
            fields=[("xa", "Ax", float), ("ya", "Ay", float), ("xc", "Cx", float), ("yc", "Cy", float)],
            solve_func=task_17.solve,
            code_str=task_17.TASK_CODE,
            format_result_func=lambda b, d: f"Точка B: {b}, Точка D: {d}"
        )

        sub_tabs.addTab(t9, "Зад. 9 (Угол прямых)")
        sub_tabs.addTab(t11, "Зад. 11 (Треугольник)")
        sub_tabs.addTab(t14, "Зад. 14 (Углы △)")
        sub_tabs.addTab(t15, "Зад. 15 (3D векторы)")
        sub_tabs.addTab(t17, "Зад. 17 (Квадрат)")

        layout.addWidget(sub_tabs)