# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: CourseSchedule
def search_courses(query: str):
    """Поиск курсов по нескольким полям без учёта регистра."""
    q = query.lower().strip()
    if not q:
        return []
    results = []
    for course in courses:
        name_lower = course['name'].lower()
        desc_lower = (course.get('description') or '').lower()
        teacher_lower = (course.get('teacher', '')).lower()
        if q in name_lower or q in desc_lower or q in teacher_lower:
            results.append(course)
    return results

def search_lectures(query: str):
    """Поиск лекций по нескольким полям без учёта регистра."""
    q = query.lower().strip()
    if not q:
        return []
    results = []
    for lecture in lectures:
        title_lower = (lecture.get('title') or '').lower()
        topic_lower = (lecture.get('topic', '')).lower()
        lecturer_lower = (lecture.get('lecturer', '')).lower()
        if q in title_lower or q in topic_lower or q in lecturer_lower:
            results.append(lecture)
    return results

def search_rooms(query: str):
    """Поиск аудиторий по нескольким полям без учёта регистра."""
    q = query.lower().strip()
    if not q:
        return []
    results = []
    for room in rooms:
        name_lower = (room.get('name') or '').lower()
        capacity_str = str(room.get('capacity', '')).lower()
        location_lower = (room.get('location', '')).lower()
        if q in name_lower or q in capacity_str or q in location_lower:
            results.append(room)
    return results

def search_attendance(query: str):
    """Поиск записей посещаемости по нескольким полям без учёта регистра."""
    q = query.lower().strip()
    if not q:
        return []
    results = []
    for record in attendance_records:
        student_lower = (record.get('student', '') or '').lower()
        course_name_lower = (record.get('course', '') or '').lower()
        date_str = str(record.get('date', '')).lower()
        if q in student_lower or q in course_name_lower or q in date_str:
            results.append(record)
    return results
