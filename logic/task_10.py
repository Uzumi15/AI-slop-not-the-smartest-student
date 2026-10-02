# Задача 10: Перевод длины из метров в русские неметрические единицы.
# 1 вершок = 44.45 мм = 0.04445 м
# 1 аршин = 16 вершков
# 1 сажень = 3 аршина
# 1 верста = 500 саженей

from typing import Tuple

TASK_CODE = '''def solve(meters: float) -> Tuple[int, int, int, float]:
    vershok_m = 0.04445
    total_vershok = meters / vershok_m
    
    verst = int(total_vershok // (500 * 3 * 16))
    rem_vershok = total_vershok % (500 * 3 * 16)
    
    sazhen = int(rem_vershok // (3 * 16))
    rem_vershok %= (3 * 16)
    
    arshin = int(rem_vershok // 16)
    vershok = rem_vershok % 16
    
    return verst, sazhen, arshin, round(vershok, 2)'''

def solve(meters: float) -> Tuple[int, int, int, float]:
    vershok_m = 0.04445
    total_vershok = meters / vershok_m
    
    verst = int(total_vershok // (500 * 3 * 16))
    rem_vershok = total_vershok % (500 * 3 * 16)
    
    sazhen = int(rem_vershok // (3 * 16))
    rem_vershok %= (3 * 16)
    
    arshin = int(rem_vershok // 16)
    vershok = rem_vershok % 16
    
    return verst, sazhen, arshin, round(vershok, 2)