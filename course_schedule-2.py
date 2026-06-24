# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: CourseSchedule
class CourseSchedule:
    def __init__(self):
        self.courses = []
        self.teachers = {}
        self.rooms = {}
    
    def add_course(self, name, description=""):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя курса должно быть непустой строкой")
        for c in self.courses:
            if c['name'].lower() == name.lower():
                return False
        self.courses.append({'id': len(self.courses) + 1, 'name': name, 'description': description})
        return True
    
    def add_teacher(self, name, subject=""):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя преподавателя должно быть непустой строкой")
        self.teachers[name] = {'id': len(self.teachers) + 1, 'name': name, 'subject': subject}
        return True
    
    def add_room(self, number, capacity=30):
        if not isinstance(number, str) or len(number.strip()) == 0:
            raise ValueError("Номер аудитории должен быть непустой строкой")
        self.rooms[number] = {'id': len(self.rooms) + 1, 'number': number, 'capacity': capacity}
        return True
    
    def add_session(self, course_name, teacher_name, room_number, date_time=""):
        if not isinstance(course_name, str) or not isinstance(teacher_name, str):
            raise ValueError("Имя курса и преподавателя должны быть строками")
        course = next((c for c in self.courses if c['name'].lower() == course_name.lower()), None)
        teacher = self.teachers.get(teacher_name)
        room = self.rooms.get(room_number)
        if not course or not teacher or not room:
            raise ValueError("Неверные данные курса, преподавателя или аудитории")
        if len(self.courses) == 0 or len(self.teachers) == 0 or len(self.rooms) == 0:
            return False
        session = {'id': len(self.courses) + len(self.teachers) + len(self.rooms), 'course_id': course['id'], 
                   'teacher_name': teacher_name, 'room_number': room_number, 'date_time': date_time}
        self.courses[-1]['sessions'].append(session) if not hasattr(course, 'sessions') else None
        return True
