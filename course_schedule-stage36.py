# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: CourseSchedule
def check_and_repair_data():
    """Проверка целостности и простой ремонт данных."""
    issues = []
    for course in courses:
        if not course['lectures']:
            issues.append(f"Курс {course['name']} не имеет лекций")
        for lecture in course['lectures']:
            if not lecture['room']:
                issues.append(f"Лекция {lecture['course_name']} не имеет аудитории")
            if not lecture['teacher']:
                issues.append(f"Лекция {lecture['course_name']} не имеет преподавателя")
    repaired = False
    for course in courses:
        if not course['lectures']:
            course['lectures'] = []
            repaired = True
        for lecture in course['lectures']:
            if not lecture.get('room'):
                lecture['room'] = 'Default Room'
                repaired = True
            if not lecture.get('teacher'):
                lecture['teacher'] = 'Unknown Teacher'
                repaired = True
    return issues, repaired
