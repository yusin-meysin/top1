# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: CourseSchedule
def format_schedule_header(course: Course) -> str:
    """Формирует аккуратный заголовок расписания курса."""
    return (
        f"Курс: {course.name}\n"
        f"Преподаватель: {course.teacher.name}\n"
        f"Аудитория: {course.room.name}\n"
        f"Семестр: {course.semester}"
    )


def format_lesson_line(lesson: Lesson) -> str:
    """Формирует строку описания одного занятия."""
    return (
        f"  {lesson.day} {lesson.time_start}-{lesson.time_end} | "
        f"{lesson.topic}\n"
    )


def format_attendance_report(record: AttendanceRecord) -> str:
    """Формирует отчёт о посещаемости студента."""
    return (
        f"Студент: {record.student.name}\n"
        f"Курс: {record.course.name}\n"
        f"Посещено: {record.attended} / {record.total}\n"
        f"Процент: {record.attendance_rate:.1f}%\n"
    )


def print_course_report(course: Course) -> None:
    """Выводит отформатированный отчёт по всему расписанию курса."""
    print(format_schedule_header(course))
    print("Расписание занятий:")
    for lesson in course.lessons:
        print(format_lesson_line(lesson))

    print("Отчёт о посещаемости:")
    for record in course.attendance:
        print(format_attendance_report(record))
