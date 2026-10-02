# Модуль форматирования и конвертации выводимых данных.


def format_angle_dms(degrees: int, minutes: int, seconds: float) -> str:
    """Форматирует угол в градусах, минутах и секундах."""
    return f"{degrees}° {minutes}' {seconds:.2f}\""

def format_time_hms(hours: int, minutes: int, seconds: int) -> str:
    """Форматирует время в чч:мм:сс."""
    return f"{hours:02d} ч {minutes:02d} мин {seconds:02d} сек"

def format_russian_length(verst: int, sazhen: int, arshin: int, vershok: float) -> str:
    """Форматирует длины в русские неметрические единицы."""
    parts = []
    if verst > 0:
        parts.append(f"{verst} верст(ы)")
    if sazhen > 0 or verst > 0:
        parts.append(f"{sazhen} саженей")
    if arshin > 0 or sazhen > 0 or verst > 0:
        parts.append(f"{arshin} аршин(а)")
    parts.append(f"{vershok:.2f} вершков")
    return ", ".join(parts)