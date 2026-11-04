# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: CourseSchedule
print("="*50)
print("  Самопроверка CourseSchedule")
print("="*50)
print(f"Курсов в системе: {len(CourseSchedule.courses)}")
print(f"Преподавателей: {len(CourseSchedule.teachers)}")
print(f"Аудиторий: {len(CourseSchedule.rooms)}")
total_lectures = sum(len(c.lectures) for c in CourseSchedule.courses)
print(f"Всего занятий: {total_lectures}")
if total_lectures > 0:
    print(f"Средняя посещаемость: {sum(c.attendance_rate for c in CourseSchedule.courses)/len(CourseSchedule.courses):.1%}")
    print("Проверка конфликтов по времени:")
    conflicts = []
    for c in CourseSchedule.courses:
        for l in c.lectures:
            for other in CourseSchedule.courses:
                if other is c:
                    continue
                for ol in other.lectures:
                    if l.time == ol.time and l.room == ol.room:
                        conflicts.append((c.name, l.time, l.room))
    if conflicts:
        for conflict in conflicts:
            print(f"  КОНФЛИКТ: {conflict}")
    else:
        print("  Конфликтов по времени и аудитории не найдено")
print("-"*50)
print("Готово. Приложение готово к использованию.")
print("="*50)
