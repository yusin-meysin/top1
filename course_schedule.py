# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: CourseSchedule
import sys
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import date

@dataclass
class Room:
    id: str
    name: str
    capacity: int

@dataclass
class Teacher:
    id: str
    full_name: str
    subject_specialty: str

@dataclass
class Lesson:
    id: str
    course_id: str
    room_id: str
    teacher_id: str
    date_time: str  # "YYYY-MM-DD HH:MM"
    attendance_count: int = 0

def create_demo_data() -> Dict[str, object]:
    rooms = [Room("R1", "Аудитория 101", 50), Room("R2", "Лабораторная А", 30)]
    teachers = [Teacher("T1", "Иванов И.И.", "Математика"), Teacher("T2", "Петрова С.С.", "Физика")]
    
    lessons: List[Lesson] = []
    for i in range(5):
        room = rooms[i % len(rooms)]
        teacher = teachers[i % len(teachers)]
        lesson = Lesson(id=f"L{i+1}", course_id="COURSE_001", room_id=room.id, teacher_id=teacher.id, date_time=date.today().strftime("%Y-%m-%d") + f" {8+i*2:02d}:00", attendance_count=i)
        lessons.append(lesson)

    return {"rooms": rooms, "teachers": teachers, "lessons": lessons}

if __name__ == "__main__":
    demo = create_demo_data()
    print(f"Загружено {len(demo['rooms'])} аудиторий и {len(demo['teachers'])} преподавателей.")
