# Задача 9: Угол между двумя прямыми y = k1*x + b1 и y = k2*x + b2.

import math
from typing import Tuple

TASK_CODE = '''def solve(k1: float, k2: float) -> Tuple[int, int]:
    denominator = 1 + k1 * k2
    if abs(denominator) < 1e-9:
        # Прямые перпендикулярны
        return 90, 0
        
    tg_phi = abs((k2 - k1) / denominator)
    phi_rad = math.atan(tg_phi)
    phi_deg_total = math.degrees(phi_rad)
    
    degrees = int(phi_deg_total)
    minutes = round((phi_deg_total - degrees) * 60)
    
    if minutes == 60:
        degrees += 1
        minutes = 0
        
    return degrees, minutes'''

def solve(k1: float, k2: float) -> Tuple[int, int]:
    denominator = 1 + k1 * k2
    if abs(denominator) < 1e-9:
        return 90, 0
        
    tg_phi = abs((k2 - k1) / denominator)
    phi_rad = math.atan(tg_phi)
    phi_deg_total = math.degrees(phi_rad)
    
    degrees = int(phi_deg_total)
    minutes = round((phi_deg_total - degrees) * 60)
    if minutes == 60:
        degrees += 1
        minutes = 0
        
    return degrees, minutes