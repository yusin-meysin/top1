# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: CourseSchedule
def print_course_record(record):
    """Компактный вывод одной записи расписания."""
    if not record:
        return
    line1 = (f"Курс: {record.course_name} | "
             f"Преподаватель: {record.instructor} | "
             f"Аудитория: {record.room}")
    line2 = (f"Группа: {', '.join(record.groups)} | "
             f"Занятия: {', '.join(record.sessions)}, "
             f"Посещаемость: {record.attendance_rate:.1f}%")
    print(line1)
    print(line2)
