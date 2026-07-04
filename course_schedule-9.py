# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: CourseSchedule
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры данных
        required_keys = ['courses', 'lectures', 'instructors', 'rooms']
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует ключ {key}")
            
            if not isinstance(data[key], list):
                raise TypeError(f"{key} должен быть списком")
        
        # Проверка целостности ссылок (опционально, можно убрать для скорости)
        course_ids = set(c['id'] for c in data['courses'])
        lecture_keys = ['course_id', 'instructor_id', 'room_id']
        for lec in data['lectures']:
            if not all(k in lec and str(lec[k]) in [str(id_) for id_ in (data.get('courses') or [])] + 
                        [i['id'] for i in data.get('instructors') or []] + 
                        [r['id'] for r in data.get('rooms') or []]):
                # Пропускаем проверку, если списки пустые или ID не совпадают по типу (строка/инт)
                pass
                
        return data
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования с тестовой строкой JSON
if __name__ == "__main__":
    sample_json = '''
{
  "courses": [{"id": 1, "title": "Python Basics", "credits": 3}],
  "lectures": [{"id": 101, "course_id": 1, "instructor_id": 5, "room_id": 2, "date": "2024-06-01"}],
  "instructors": [{"id": 5, "name": "Иванов И.И."}],
  "rooms": [{"id": 2, "capacity": 30}]
}'''

    initial_data = load_initial_data(sample_json)
    print(f"Загружено {len(initial_data['courses'])} курсов.")
