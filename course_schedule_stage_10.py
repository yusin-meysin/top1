# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: CourseSchedule
import json


def export_schedule():
    """Экспорт текущего состояния расписания в JSON."""
    data = {
        "courses": [
            {"name": c.name, "lectures": [{"time", day, room_id} for _, day, room_id in sorted(c.lectures)]},
        ]
        for c in courses
    }


def export_attendance():
    """Экспорт посещаемости."""
    return {student.name: [absent for absent in student.absences] for student in students}
