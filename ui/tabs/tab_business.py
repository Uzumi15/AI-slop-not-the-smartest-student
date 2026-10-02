# Это вкладка бизнес-задач и экономики (Задачи 5, 6, 16).

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.tabs.base_task_widget import TaskCardWidget
from logic import task_05, task_06, task_16

class BusinessTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        sub_tabs = QTabWidget()

        # Задача 5
        t5 = TaskCardWidget(
            task_num=5,
            title="Накопления коммерсанта",
            description="Расчет количества лет для накопления суммы S при стартовом капитале k и ежемесячном приросте p%.",
            fields=[("k", "Старт. капитал k (руб)", float), ("p", "Прирост p (%/мес)", float), ("S", "Цена магазина S (руб)", float)],
            solve_func=task_05.solve,
            code_str=task_05.TASK_CODE,
            format_result_func=lambda years: f"Необходимо лет: {years}"
        )

        # Задача 6
        t6 = TaskCardWidget(
            task_num=6,
            title="Размножение семян селекционера",
            description="Расчет количества лет для накопления семян на поле S га с нормой высева n кг/га.",
            fields=[("k", "Семян собрано k (кг)", float), ("p", "Урожайность p (кг/кг)", float), ("S", "Площадь поля S (га)", float), ("n", "Норма n (кг/га)", float)],
            solve_func=task_06.solve,
            code_str=task_06.TASK_CODE,
            format_result_func=lambda years: f"Необходимо лет: {years}"
        )

        # Задача 16
        t16 = TaskCardWidget(
            task_num=16,
            title="Цена молока животновода",
            description="Динамика цены молока при ежезимнем повышении на p% и ежелетнем снижении на p% через n лет.",
            fields=[("price", "Нач. цена (руб)", float), ("p", "Процент p (%)", float), ("n", "Лет (n)", int)],
            solve_func=task_16.solve,
            code_str=task_16.TASK_CODE,
            format_result_func=lambda p_end, diff, status: f"Итоговая цена: {p_end} руб.<br>Динамика: {status} на {diff} руб."
        )

        sub_tabs.addTab(t5, "Зад. 5 (Коммерсант)")
        sub_tabs.addTab(t6, "Зад. 6 (Селекционер)")
        sub_tabs.addTab(t16, "Зад. 16 (Молоко)")

        layout.addWidget(sub_tabs)