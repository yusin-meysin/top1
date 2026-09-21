# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: CourseSchedule
def migrate_structure():
    """Миграция структуры данных: добавление новых полей в CourseSchedule."""
    # Проверяем текущую версию структуры данных
    current_version = get_data_version()
    
    if current_version == "v1":
        # v1 -> v2: Добавляем список преподавателей и аудиторий
        courses = get_courses()
        for course in courses:
            if "instructors" not in course:
                course["instructors"] = []
            if "rooms" not in course:
                course["rooms"] = []
        save_data()
        print("Миграция v1 -> v2 завершена")
    
    elif current_version == "v2":
        # v2 -> v3: Добавляем посещаемость и статусы
        courses = get_courses()
        for course in courses:
            if "attendance" not in course:
                course["attendance"] = {}
            if "status" not in course:
                course["status"] = "active"
        save_data()
        print("Миграция v2 -> v3 завершена")
    
    else:
        print("Текущая версия не поддерживается для миграции")

migrate_structure()
