# Модуль валидации пользовательского ввода из GUI.


def parse_float(value: str, field_name: str) -> float:
    """
    Парсит строку в число с плавающей точкой.
    Поддерживает ввод как с точкой, так и с запятой.
    """
    clean_val = value.strip().replace(',', '.')
    if not clean_val:
        raise ValueError(f"Поле '{field_name}' не должно быть пустым.")
    try:
        return float(clean_val)
    except ValueError:
        raise ValueError(f"Поле '{field_name}' должно содержать число (получено: '{value}').")

def parse_int(value: str, field_name: str) -> int:
    """
    Парсит строку в целое число.
    """
    clean_val = value.strip()
    if not clean_val:
        raise ValueError(f"Поле '{field_name}' не должно быть пустым.")
    try:
        return int(clean_val)
    except ValueError:
        raise ValueError(f"Поле '{field_name}' должно быть целым числом (получено: '{value}').")

def validate_positive(value: float, field_name: str, allow_zero: bool = False) -> float:
    """
    Проверяет, что число положительное.
    """
    if allow_zero and value < 0:
        raise ValueError(f"Поле '{field_name}' должно быть неотрицательным (≥ 0).")
    if not allow_zero and value <= 0:
        raise ValueError(f"Поле '{field_name}' должно быть строго больше 0.")
    return value