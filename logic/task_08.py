# Задача 8: Представление комплексного числа z = x + iy в тригонометрической форме.

import math
from typing import Tuple

TASK_CODE = '''def solve(x: float, y: float) -> Tuple[float, float, str]:
    r = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)  # Учитывает все четверти плоскости
    expr = f"z = {r:.4f} * (cos({phi:.4f}) + i*sin({phi:.4f}))"
    return r, phi, expr'''

def solve(x: float, y: float) -> Tuple[float, float, str]:
    r = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    expr = f"z = {r:.4f} * (cos({phi:.4f}) + i*sin({phi:.4f}))"
    return r, phi, expr