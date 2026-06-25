# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: CourseSchedule
class CourseSchedule:
    def __init__(self):
        self._courses = {}
        self._lectures = []
        self._teachers = set()
        self._rooms = set()
    
    def add_teacher(self, name: str) -> None:
        if not name.strip(): return
        self._teachers.add(name)
    
    def add_room(self, room_id: str) -> None:
        if not room_id.strip(): return
        self._rooms.add(room_id)
    
    def create_course(self, course_name: str, teacher: str, room: str) -> dict | None:
        if teacher not in self._teachers or room not in self._rooms:
            return None
        self._courses[course_name] = {'teacher': teacher, 'room': room}
        return self._courses[course_name]
    
    def add_lecture(self, course_name: str, date: str, time_start: int, time_end: int) -> dict | None:
        if course_name not in self._courses:
            return None
        lecture = {
            'date': date,
            'time_start': time_start,
            'time_end': time_end,
            'attendance': 0
        }
        self._lectures.append({**lecture, **self._courses[course_name]})
        return lecture
    
    def mark_attendance(self, course_name: str, date: str) -> int | None:
        for lec in self._lectures:
            if (lec['course'] == course_name and 
                lec['date'] == date):
                lec['attendance'] += 1
                return lec['attendance']
        return None
