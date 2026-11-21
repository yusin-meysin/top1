# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: CourseSchedule
def bulk_update_records():
    print("Массовое обновление выбранных записей")
    if not courses:
        print("Нет курсов для редактирования")
        return
    print("Выберите записи для обновления (введите их номера через пробел или 'all')")
    selection = input("> ").strip()
    if selection.lower() == "all":
        selected = courses
    else:
        selected = [courses[int(x)] for x in selection.split() if x.isdigit() and int(x) < len(courses)]
    if not selected:
        print("Ничего не выбрано")
        return
    print(f"Обновление {len(selected)} записей")
    for course in selected:
        print(f"Курс {course.id}: {course.name}")
        print("1) Изменить название")
        print("2) Изменить преподавателя")
        print("3) Изменить аудиторию")
        print("4) Изменить время")
        print("5) Пропустить")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            course.name = input("Новое название: ").strip()
        elif choice == "2":
            course.teacher = input("Новый преподаватель: ").strip()
        elif choice == "3":
            course.room = input("Новая аудитория: ").strip()
        elif choice == "4":
            course.time = input("Новое время: ").strip()
        elif choice != "5":
            print("Неверный выбор")
    print("Массовое обновление завершено")
