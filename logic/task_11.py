# Задача 11: Стороны равнобедренного прямоугольного треугольника по высоте h.
# В таком треугольнике:
# гипотенуза c = 2 * h
# катеты a = b = h * sqrt(2)

import math
from typing import Tuple

TASK_CODE = '''def solve(h: float) -> Tuple[float, float, float]:
    c = 2.0 * h
    a = h * math.sqrt(2)
    b = a
    return round(a, 4), round(b, 4), round(c, 4)'''

def solve(h: float) -> Tuple[float, float, float]:
    c = 2.0 * h
    a = h * math.sqrt(2)
    b = a
    return round(a, 4), round(b, 4), round(c, 4)