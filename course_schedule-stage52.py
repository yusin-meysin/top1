# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: CourseSchedule
def export_report(schedule):
    lines = []
    lines.append("Отчёт по расписанию учебных курсов")
    lines.append("=" * 40)
    for course in schedule.courses:
        lines.append(f"Курс: {course.name}")
        for lesson in course.lessons:
            attended = sum(1 for r in lesson.attendance if r.attended)
            lines.append(f"  {lesson.day} {lesson.time} ({lesson.room}) - {lesson.name}")
            lines.append(f"    Преподаватель: {lesson.teacher.name}")
            lines.append(f"    Посещаемость: {attended}/{lesson.attendance_count}")
        lines.append("-" * 40)
    return "\n".join(lines)
