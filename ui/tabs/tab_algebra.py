# Это вкладка алгебры и функций (Задачи 7, 8, 12, 13, 18).


from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.tabs.base_task_widget import TaskCardWidget
from logic import task_07, task_08, task_12, task_13, task_18

class AlgebraTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        sub_tabs = QTabWidget()

        # Задача 7
        t7 = TaskCardWidget(
            task_num=7,
            title="Коэффициенты кубического уравнения",
            description="Восстановление коэффициентов уравнения x³ + Bx² + Cx + D = 0 по его корням a, b, c.",
            fields=[("a", "Корень a", float), ("b", "Корень b", float), ("c", "Корень c", float)],
            solve_func=task_07.solve,
            code_str=task_07.TASK_CODE,
            format_result_func=lambda A, B, C, D: f"x³ + ({B:.2f})x² + ({C:.2f})x + ({D:.2f}) = 0"
        )

        # Задача 8
        t8 = TaskCardWidget(
            task_num=8,
            title="Тригонометрическая форма комплексного числа",
            description="Перевод z = x + iy в вид z = r(cos φ + i sin φ).",
            fields=[("x", "Действительная часть (x)", float), ("y", "Мнимая часть (y)", float)],
            solve_func=task_08.solve,
            code_str=task_08.TASK_CODE,
            format_result_func=lambda r, phi, expr: f"{expr}<br><b>Модуль r:</b> {r:.4f}, <b>Аргумент φ:</b> {phi:.4f} рад"
        )

        # Задача 12
        t12 = TaskCardWidget(
            task_num=12,
            title="Вершина параболы",
            description="Нахождение координат вершины (x₀, y₀) параболы y = ax² + bx + c.",
            fields=[("a", "Коэффициент a", float), ("b", "Коэффициент b", float), ("c", "Коэффициент c", float)],
            solve_func=task_12.solve,
            code_str=task_12.TASK_CODE,
            format_result_func=lambda x0, y0: f"Вершина параболы: (x₀ = {x0}, y₀ = {y0})"
        )

        # Задача 13
        t13 = TaskCardWidget(
            task_num=13,
            title="Аппроксимация sin(x)",
            description="Вычисление sin(x) по формуле Тейлора (y = x - x³/6 + x⁵/120) и сравнение с точным значением.",
            fields=[("x", "Аргумент x (в радианах)", float)],
            solve_func=task_13.solve,
            code_str=task_13.TASK_CODE,
            format_result_func=lambda approx, exact, diff: f"Аппроксимация: {approx}<br>Точное значение: {exact}<br>Погрешность: {diff}"
        )

        # Задача 18
        t18 = TaskCardWidget(
            task_num=18,
            title="Квадратное уравнение и проверка погрешности",
            description="Нахождение корней ax² + bx + c = 0 (D > 0) и вычисление погрешности подстановкой.",
            fields=[("a", "Коэффициент a", float), ("b", "Коэффициент b", float), ("c", "Коэффициент c", float)],
            solve_func=task_18.solve,
            code_str=task_18.TASK_CODE,
            format_result_func=lambda x1, x2, err1, err2: f"x₁ = {x1} (погрешность: {err1})<br>x₂ = {x2} (погрешность: {err2})"
        )

        sub_tabs.addTab(t7, "Зад. 7 (Куб. ур-ние)")
        sub_tabs.addTab(t8, "Зад. 8 (Комплексные)")
        sub_tabs.addTab(t12, "Зад. 12 (Парабола)")
        sub_tabs.addTab(t13, "Зад. 13 (Aппроксимация)")
        sub_tabs.addTab(t18, "Зад. 18 (Квадр. ур-ние)")

        layout.addWidget(sub_tabs)