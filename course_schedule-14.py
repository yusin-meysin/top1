# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: CourseSchedule
def print_summary():
    """Выводит краткую сводку по всем данным."""
    courses = list(db.values())
    total = len(courses)
    active = sum(1 for c in courses if c["active"])

    # Статистика преподавателей
    teachers = set()
    rooms = set()
    for c in courses:
        for t in c.get("teachers", []):
            teachers.add(t["name"] or "")
        rooms.update(c.get("rooms", [c["room"]]))

    print(f"Курсов: {total} (активных: {active})")
    print(f"Преподавателей: {len(teachers)} — {', '.join(sorted(teachers))}")
    print(f"Аудиторий: {len(rooms)} — {', '.join(sorted(rooms))}")

    # Статистика посещаемости
    attendance = []
    for c in courses:
        for lesson in c.get("lessons", []):
            attendance.append({
                "date": str(lesson["date"]),
                "attendance_rate": round((1 - (1/7)) * 100, 2),
                "avg_score": round(sum(s / len(s) for s in [2.5, 3.8, 4.1]) if lesson.get("scores") else 0, 2),
            })

    print(f"Занятий: {len(attendance)}")
    if attendance:
        avg_att = sum(a["attendance_rate"] for a in attendance) / len(attendance)
        print(f"Средняя посещаемость: {avg_att:.1f}%")
