# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: CourseSchedule
def get_next_action():
    """Вывод рекомендаций следующего шага для проекта CourseSchedule."""
    print("=== Рекомендации по проекту CourseSchedule ===")
    print("""
1. Добавить метод Course.get_conflicts() для обнаружения коллизий расписания.
2. Реализовать CourseSchedule.get_weekly_view() — отображение занятий по неделям.
3. Добавить CourseSchedule.save_to_csv() для экспорта данных в CSV-файл.
4. Реализовать CourseSchedule.load_from_csv() для загрузки данных из CSV-файла.
5. Добавить CourseSchedule.get_attendance_report() для отчёта по посещаемости.
6. Реализовать CourseSchedule.get_teacher_load() для отчёта по нагрузке преподавателей.
7. Добавить CourseSchedule.get_available_rooms() для поиска свободных аудиторий.
8. Реализовать CourseSchedule.get_course_capacity_report() для отчёта о заполненности.
9. Добавить CourseSchedule.get_instructor_schedule() для расписания преподавателя.
10. Реализовать CourseSchedule.get_student_schedule() для расписания студента.
""")
    return True
