# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: CourseSchedule
def demo_run():
    import random
    random.seed(42)
    print("=== Демо-тестирование CourseSchedule ===")
    for i in range(1, 6):
        course = Course(name=f"Курс-{i:02d}", description=f"Описание курса {i}")
        teacher = Teacher(fullname=f"Иванов И{random.randint(1,5)}ич", email=f"t{i}@university.edu")
        room = Room(name=f"Aудитория-{random.choice(['B','C','D'])}{random.randint(10,99):02d}", capacity=random.randint(30, 200))
        session = Session(course=course, teacher=teacher, room=room, date=f"2026-05-1{i}", time_start="08:00", time_end="10:00")
        attendance = Attendance(session=session, student_name=f"Студент-{random.randint(100,999)}", present=True)
        print(f"[{i}] {course.name} | {teacher.fullname} | {room.name} | {session.date} | {attendance.present}")

demo_run()
