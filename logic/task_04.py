# Задача 4: Расчет продолжительности промежутка времени в пределах суток.

from typing import Tuple

TASK_CODE = '''def solve(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> Tuple[int, int, int]:
    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2
    
    duration_sec = end_sec - start_sec
    if duration_sec < 0:
        duration_sec += 24 * 3600  # Переход через полночь
        
    hours = duration_sec // 3600
    minutes = (duration_sec % 3600) // 60
    seconds = duration_sec % 60
    
    return hours, minutes, seconds'''

def solve(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> Tuple[int, int, int]:
    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2
    
    duration_sec = end_sec - start_sec
    if duration_sec < 0:
        duration_sec += 24 * 3600
        
    hours = duration_sec // 3600
    minutes = (duration_sec % 3600) // 60
    seconds = duration_sec % 60
    
    return hours, minutes, seconds