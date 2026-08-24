# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: CourseSchedule
def print_project_metrics():
    """Проектные метрики: количество сущностей и записей."""
    metrics = {
        "Курсы": len(courses),
        "Преподаватели": len(teachers),
        "Аудитории": len(rooms),
        "Занятия": len(lectures),
        "Посещения": len(attendances),
    }
    total = sum(metrics.values())
    print("=== Метрики проекта CourseSchedule ===")
    for name, count in metrics.items():
        print(f"{name}: {count}")
    print(f"Всего записей: {total}")
