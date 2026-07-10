# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: CourseSchedule
import json, sys, os

def load_json(path):
    if not os.path.exists(path):
        print(f"Файл {path} не найден.")
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            return [data]
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON в {path}: {e}")
        return None

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "schedule.json"
    courses = load_json(path)
    if courses is not None:
        print(f"Загружено курсов: {len(courses)}")
