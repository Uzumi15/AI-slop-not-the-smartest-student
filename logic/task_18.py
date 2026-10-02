# Задача 18: Корни квадратного уравнения с положительным дискриминантом и проверка погрешности.
# ax^2 + bx + c = 0



import math
from typing import Tuple

TASK_CODE = '''def solve(a: float, b: float, c: float) -> Tuple[float, float, float, float]:
    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен 0")
        
    D = b**2 - 4 * a * c
    if D <= 0:
        raise ValueError("Дискриминант должен быть строго больше 0")
        
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    
    err1 = abs(a * x1**2 + b * x1 + c)
    err2 = abs(a * x2**2 + b * x2 + c)
    
    return round(x1, 6), round(x2, 6), round(err1, 8), round(err2, 8)'''

def solve(a: float, b: float, c: float) -> Tuple[float, float, float, float]:
    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен 0")
    D = b**2 - 4 * a * c
    if D <= 0:
        raise ValueError("Дискриминант должен быть строго больше 0")
        
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    
    err1 = abs(a * x1**2 + b * x1 + c)
    err2 = abs(a * x2**2 + b * x2 + c)
    
    return round(x1, 6), round(x2, 6), round(err1, 8), round(err2, 8)