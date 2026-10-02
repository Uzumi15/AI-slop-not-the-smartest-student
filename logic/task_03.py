# Задача 3: Перевод длины из дюймов в метры, сантиметры и миллиметры.

from typing import Tuple

TASK_CODE = '''def solve(inches: float) -> Tuple[int, int, float]:
    # 1 дюйм = 2.54 см = 0.0254 м = 25.4 мм
    total_mm = inches * 25.4
    
    meters = int(total_mm // 1000)
    remainder_mm = total_mm % 1000
    
    centimeters = int(remainder_mm // 10)
    millimeters = remainder_mm % 10
    
    return meters, centimeters, round(millimeters, 2)'''

def solve(inches: float) -> Tuple[int, int, float]:
    total_mm = inches * 25.4
    meters = int(total_mm // 1000)
    remainder_mm = total_mm % 1000
    centimeters = int(remainder_mm // 10)
    millimeters = remainder_mm % 10
    return meters, centimeters, round(millimeters, 2)