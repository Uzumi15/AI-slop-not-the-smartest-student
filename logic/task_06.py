# Задача 6: Расчет времени для размножения семян селекционером.

TASK_CODE = '''def solve(k: float, p: float, S: float, n: float) -> int:
    required_seeds = S * n  # Всего кг семян нужно для поля S га
    if k >= required_seeds:
        return 0
    if p <= 1:
        raise ValueError("Коэффициент размножения p должен быть больше 1")
        
    years = 0
    current_seeds = k
    while current_seeds < required_seeds:
        current_seeds = current_seeds * p
        years += 1
        
    return years'''

def solve(k: float, p: float, S: float, n: float) -> int:
    required_seeds = S * n
    if k >= required_seeds:
        return 0
    if p <= 1:
        raise ValueError("Коэффициент размножения p должен быть больше 1")
        
    years = 0
    current_seeds = k
    while current_seeds < required_seeds:
        current_seeds *= p
        years += 1
        
    return years