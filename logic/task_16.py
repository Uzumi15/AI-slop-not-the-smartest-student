# Задача 16: Изменение цены на молоко через n лет.



from typing import Tuple

TASK_CODE = '''def solve(price: float, p: float, n: int) -> Tuple[float, float, str]:
    current_price = price
    for _ in range(n):
        current_price *= (1 + p / 100.0)  # Зима
        current_price *= (1 - p / 100.0)  # Лето
        
    diff = current_price - price
    status = "Уменьшилась" if diff < 0 else ("Увеличилась" if diff > 0 else "Не изменилась")
    
    return round(current_price, 2), round(abs(diff), 2), status'''

def solve(price: float, p: float, n: int) -> Tuple[float, float, str]:
    current_price = price
    for _ in range(n):
        current_price *= (1 + p / 100.0)
        current_price *= (1 - p / 100.0)
        
    diff = current_price - price
    status = "Уменьшилась" if diff < 0 else ("Увеличилась" if diff > 0 else "Не изменилась")
    return round(current_price, 2), round(abs(diff), 2), status