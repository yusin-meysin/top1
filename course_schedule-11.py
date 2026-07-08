# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: CourseSchedule
import json

def save_data(data, filename="courses.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

if __name__ == "__main__":
    save_data(courses)
