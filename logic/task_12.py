# Задача 12: Координаты вершины параболы y = ax^2 + bx + c.
# x0 = -b / (2a)
# y0 = c - (b^2 / (4a))

from typing import Tuple

TASK_CODE = '''def solve(a: float, b: float, c: float) -> Tuple[float, float]:
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен 0 для параболы")
    x0 = -b / (2 * a)
    y0 = a * x0**2 + b * x0 + c
    return round(x0, 4), round(y0, 4)'''

def solve(a: float, b: float, c: float) -> Tuple[float, float]:
    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен 0")
    x0 = -b / (2 * a)
    y0 = a * x0**2 + b * x0 + c
    return round(x0, 4), round(y0, 4)