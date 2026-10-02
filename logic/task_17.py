# Задача 17: Нахождение противоположных вершин B и D квадрата по A и C.
#Центр O = (A + C) / 2
#Вектор OC = C - O
#Поворот на 90 градусов: (-dY, dX)



from typing import Tuple

TASK_CODE = '''def solve(xa: float, ya: float, xc: float, yc: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    xo = (xa + xc) / 2.0
    yo = (ya + yc) / 2.0
    
    dx = xc - xo
    dy = yc - yo
    
    # Вершины B и D
    xb, yb = xo - dy, yo + dx
    xd, yd = xo + dy, yo - dx
    
    return (round(xb, 2), round(yb, 2)), (round(xd, 2), round(yd, 2))'''

def solve(xa: float, ya: float, xc: float, yc: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    xo = (xa + xc) / 2.0
    yo = (ya + yc) / 2.0
    
    dx = xc - xo
    dy = yc - yo
    
    xb, yb = xo - dy, yo + dx
    xd, yd = xo + dy, yo - dx
    
    return (round(xb, 2), round(yb, 2)), (round(xd, 2), round(yd, 2))