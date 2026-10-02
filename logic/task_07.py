# Задача 7: Восстановление коэффициентов кубического уравнения по корням a, b, c.
# Формула: (x - a)(x - b)(x - c) = x^3 - (a+b+c)x^2 + (ab+bc+ac)x - abc = 0

from typing import Tuple

TASK_CODE = '''def solve(a: float, b: float, c: float) -> Tuple[float, float, float, float]:
    # Уравнение вида A*x^3 + B*x^2 + C*x + D = 0 при A = 1
    A = 1.0
    B = -(a + b + c)
    C = a * b + b * c + a * c
    D = -(a * b * c)
    return A, B, C, D'''

def solve(a: float, b: float, c: float) -> Tuple[float, float, float, float]:
    A = 1.0
    B = -(a + b + c)
    C = a * b + b * c + a * c
    D = -(a * b * c)
    return A, B, C, D