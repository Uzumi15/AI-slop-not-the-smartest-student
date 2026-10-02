# Задача 13: Аппроксимация sin(x) по формуле y = x - x^3/6 + x^5/120 и сравнение с math.sin(x).

import math
from typing import Tuple

TASK_CODE = '''def solve(x: float) -> Tuple[float, float, float]:
    y_approx = x - (x**3 / 6.0) + (x**5 / 120.0)
    y_exact = math.sin(x)
    diff = abs(y_approx - y_exact)
    return round(y_approx, 6), round(y_exact, 6), round(diff, 6)'''

def solve(x: float) -> Tuple[float, float, float]:
    y_approx = x - (x**3 / 6.0) + (x**5 / 120.0)
    y_exact = math.sin(x)
    diff = abs(y_approx - y_exact)
    return round(y_approx, 6), round(y_exact, 6), round(diff, 6)