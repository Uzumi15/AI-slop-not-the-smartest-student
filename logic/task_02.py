# Задача 2: Перевод угла из радиан в градусы, минуты и секунды.
import math
from typing import Tuple

TASK_CODE = '''def solve(rad: float) -> Tuple[int, int, float]:
    total_deg = math.degrees(rad)
    sign = -1 if total_deg < 0 else 1
    abs_deg = abs(total_deg)
    
    degrees = int(abs_deg)
    remainder_minutes = (abs_deg - degrees) * 60.0
    minutes = int(remainder_minutes)
    seconds = (remainder_minutes - minutes) * 60.0
    
    return sign * degrees, minutes, round(seconds, 4)'''

def solve(rad: float) -> Tuple[int, int, float]:
    total_deg = math.degrees(rad)
    sign = -1 if total_deg < 0 else 1
    abs_deg = abs(total_deg)
    
    degrees = int(abs_deg)
    remainder_minutes = (abs_deg - degrees) * 60.0
    minutes = int(remainder_minutes)
    seconds = (remainder_minutes - minutes) * 60.0
    
    return sign * degrees, minutes, round(seconds, 4)