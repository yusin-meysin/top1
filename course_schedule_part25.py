# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: CourseSchedule
def parse_date(date_str):
    """Parse date string in format 'YYYY-MM-DD' and return tuple (year, month, day)."""
    if not isinstance(date_str, str) or len(date_str.split('-')) != 3:
        raise ValueError(f"Некорректная дата: '{date_str}'. Ожидаемый формат: YYYY-MM-DD")
    try:
        parts = [int(x) for x in date_str.split('-')]
    except ValueError:
        raise ValueError(f"Некорректные числа в дате: '{date_str}'")

    year, month, day = parts

    if not (1 <= year <= 9999):
        raise ValueError(f"Недопустимый год: {year}")
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months[1] = 29
    if not (1 <= month <= 12):
        raise ValueError(f"Недопустимый месяц: {month}")
    if not (1 <= day <= months[month - 1]):
        raise ValueError(f"Недопустимый день для месяца {month}: {day} (максимум: {months[month - 1]})")

    return year, month, day
