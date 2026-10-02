# Задача 5: Расчет количества лет для накопления суммы коммерсантом.
TASK_CODE = '''def solve(k: float, p: float, S: float) -> float:
    if k >= S:
        return 0.0
    if p <= 0:
        raise ValueError("Процент p должен быть больше 0 для роста капитала")
        
    current = k
    months = 0
    while current < S:
        current += current * (p / 100.0)
        months += 1
        
    return round(months / 12.0, 2)'''

def solve(k: float, p: float, S: float) -> float:
    if k >= S:
        return 0.0
    if p <= 0:
        raise ValueError("Процент p должен быть больше 0")
        
    current = k
    months = 0
    while current < S:
        current += current * (p / 100.0)
        months += 1
        
    return round(months / 12.0, 2)