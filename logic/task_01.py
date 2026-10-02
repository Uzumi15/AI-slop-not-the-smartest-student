# Задача 1: Перевод угла из градусов, минут и секунд в радианы.

import math

TASK_CODE = '''def solve(deg: float, minutes: float, seconds: float) -> float:
    # Приводим все к единым градусам (со знаком)
    sign = -1 if deg < 0 or minutes < 0 or seconds < 0 else 1
    abs_deg = abs(deg) + abs(minutes) / 60.0 + abs(seconds) / 3600.0
    total_deg = sign * abs_deg
    
    # Перевод в радианы с максимальной точностью float
    radians = math.radians(total_deg)
    return radians'''

def solve(deg: float, minutes: float, seconds: float) -> float:
    sign = -1 if (deg < 0 or minutes < 0 or seconds < 0) else 1
    abs_deg = abs(deg) + abs(minutes) / 60.0 + abs(seconds) / 3600.0
    total_deg = sign * abs_deg
    return math.radians(total_deg)