# Задача 14: Внутренние углы треугольника по координатам трех вершин A, B, C.


import math
from typing import Tuple

TASK_CODE = '''def solve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float, float]:
    # Длины сторон
    a = math.hypot(x3 - x2, y3 - y2)  # BC
    b = math.hypot(x3 - x1, y3 - y1)  # AC
    c = math.hypot(x2 - x1, y2 - y1)  # AB
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Точки лежат на одной прямой или совпадают")
        
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180.0 - angle_A - angle_B
    
    return round(angle_A, 2), round(angle_B, 2), round(angle_C, 2)'''

def solve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> Tuple[float, float, float]:
    a = math.hypot(x3 - x2, y3 - y2)
    b = math.hypot(x3 - x1, y3 - y1)
    c = math.hypot(x2 - x1, y2 - y1)
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Точки не образуют треугольник")
        
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180.0 - angle_A - angle_B
    
    return round(angle_A, 2), round(angle_B, 2), round(angle_C, 2)