# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: CourseSchedule
def parse_time_str(t):
    """Parse 'HH:MM' or 'HH:MM:SS' -> (h, m, s) ints."""
    parts = t.split(':')
    return (int(parts[0]), int(parts[1]), int(parts[2] if len(parts) == 3 else 0))
