# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: CourseSchedule
def reset_demo_data():
    """Сбросить все демо-данные в начальные значения и вернуть True."""
    global courses, lectures, teachers, rooms, attendance
    
    # Сброс курсов
    if courses == []:
        courses = [
            {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы Python'},
            {'id': 2, 'name': 'Алгоритмы и структуры данных', 'description': 'Классические алгоритмы'},
            {'id': 3, 'name': 'Машинное обучение', 'description': 'Введение в ML'}
        ]
    
    # Сброс преподавателей
    if teachers == []:
        teachers = [
            {'id': 1, 'first_name': 'Алексей', 'last_name': 'Иванов'},
            {'id': 2, 'first_name': 'Мария', 'last_name': 'Петрова'}
        ]
    
    # Сброс аудиторий
    if rooms == []:
        rooms = [
            {'id': 1, 'name': 'А-101'},
            {'id': 2, 'name': 'Б-205'},
            {'id': 3, 'name': 'В-310'}
        ]
    
    # Сброс занятий и посещаемости
    if lectures == []:
        lectures = [
            {'course_id': 1, 'teacher_id': 1, 'room_id': 1, 'time_slot': 'ПН 9:00', 'attendance_count': 25},
            {'course_id': 1, 'teacher_id': 1, 'room_id': 2, 'time_slot': 'СР 14:00', 'attendance_count': 28},
            {'course_id': 2, 'teacher_id': 2, 'room_id': 3, 'time_slot': 'ВТ 10:00', 'attendance_count': 22},
            {'course_id': 3, 'teacher_id': 1, 'room_id': 1, 'time_slot': 'ЧТ 15:00', 'attendance_count': 20}
        ]
    
    if attendance == []:
        attendance = [
            {'student_name': 'Иванов И.И.', 'lecture_id': 1, 'present': True},
            {'student_name': 'Петрова А.А.', 'lecture_id': 1, 'present': True},
            {'student_name': 'Сидоров П.П.', 'lecture_id': 2, 'present': False}
        ]
    
    return True

def clear_all_data():
    """Очистить все данные и вернуть пустые структуры."""
    global courses, lectures, teachers, rooms, attendance
    
    courses = []
    lectures = []
    teachers = []
    rooms = []
    attendance = []
    
    return True
