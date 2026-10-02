# Задача 15: Угол между 3D векторами A и B.


import math

TASK_CODE = '''def solve(xa: float, ya: float, za: float, xb: float, yb: float, zb: float) -> float:
    dot_product = xa * xb + ya * yb + za * zb
    mag_a = math.sqrt(xa**2 + ya**2 + za**2)
    mag_b = math.sqrt(xb**2 + yb**2 + zb**2)
    
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Длина вектора не может быть нулевой")
        
    cos_phi = max(-1.0, min(1.0, dot_product / (mag_a * mag_b)))
    phi_deg = math.degrees(math.acos(cos_phi))
    
    return round(phi_deg, 2)'''

def solve(xa: float, ya: float, za: float, xb: float, yb: float, zb: float) -> float:
    dot_product = xa * xb + ya * yb + za * zb
    mag_a = math.sqrt(xa**2 + ya**2 + za**2)
    mag_b = math.sqrt(xb**2 + yb**2 + zb**2)
    
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Длина вектора не может быть равной нулю")
        
    cos_phi = max(-1.0, min(1.0, dot_product / (mag_a * mag_b)))
    phi_deg = math.degrees(math.acos(cos_phi))
    
    return round(phi_deg, 2)