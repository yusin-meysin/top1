# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: CourseSchedule
def create_template(course_name, lecturer_name, lecturer_email, room, start_time, end_time, weekday):
    """Создаёт шаблон записи: 1 занятие, 1 преподаватель, 1 аудитория."""
    return {
        "course_name": course_name,
        "lecturer_name": lecturer_name,
        "lecturer_email": lecturer_email,
        "room": room,
        "start_time": start_time,
        "end_time": end_time,
        "weekday": weekday,
    }

def apply_template(template, db):
    """Применяет шаблон: создаёт запись, преподавателя и аудиторию."""
    course = db["courses"].add_record(template["course_name"])
    lecturer = db["lecturers"].add_record({"name": template["lecturer_name"], "email": template["lecturer_email"]})
    room = db["rooms"].add_record({"name": template["room"]})
    db["lecturer_courses"].add_record({"lecturer_id": lecturer["id"], "course_id": course["id"]})
    db["lecturer_rooms"].add_record({"lecturer_id": lecturer["id"], "room_id": room["id"]})
    db["course_rooms"].add_record({"course_id": course["id"], "room_id": room["id"]})
    db["lecturer_courses_rooms"].add_record({
        "lecturer_id": lecturer["id"],
        "course_id": course["id"],
        "room_id": room["id"],
        "start_time": template["start_time"],
        "end_time": template["end_time"],
        "weekday": template["weekday"],
    })
    return course, lecturer, room
