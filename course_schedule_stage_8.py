# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: CourseSchedule
import sys
from typing import Dict, List, Optional

def print_menu() -> None:
    """Отображает текстовое меню действий."""
    print("\n=== Меню CourseSchedule ===")
    print("1. Показать все курсы")
    print("2. Добавить новый курс")
    print("3. Удалить курс по ID")
    print("4. Выход")
    print("==========================\n")

def get_int_input(prompt: str) -> int:
    """Запрашивает целое число у пользователя."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def run_text_interface(courses: Dict[str, dict]) -> None:
    """Запускает текстовый интерфейс команд с меню действий."""
    while True:
        print_menu()
        choice = get_int_input("Выберите действие (1-4): ")

        if choice == 1:
            if not courses:
                print("\nКурсы отсутствуют.")
            else:
                for course_id, data in sorted(courses.items()):
                    print(f"\n--- Курс {course_id} ---")
                    print(f"Название: {data.get('name', 'N/A')}")
                    print(f"Преподаватель: {data.get('instructor', 'N/A')}")
                    print(f"Аудитория: {data.get('room', 'N/A')}")

        elif choice == 2:
            name = input("Введите название курса: ")
            instructor = input("Введите имя преподавателя: ")
            room = input("Введите номер аудитории: ")
            if not all([name, instructor, room]):
                print("Ошибка: заполните все поля.")
                continue
            course_id = f"COURSE_{len(courses) + 1}"
            courses[course_id] = {
                "name": name,
                "instructor": instructor,
                "room": room
            }
            print(f"Курс '{name}' добавлен с ID: {course_id}")

        elif choice == 3:
            course_id = input("Введите ID курса для удаления (или 'q' чтобы отменить): ")
            if course_id.lower() in ('q', ''):
                continue
            if course_id in courses:
                del courses[course_id]
                print(f"Курс '{course_id}' удалён.")
            else:
                print("Курс с таким ID не найден.")

        elif choice == 4:
            print("Завершение работы программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
