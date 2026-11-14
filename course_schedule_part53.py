# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: CourseSchedule
def import_records(path):
    """Импорт записей из простого текстового формата.

    Формат файла:
    КЛЮЧ;значение
    Например:
    name;Иван Иванов
    course;Математика
    teacher;Петрова
    room;301
    """
    records = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ";" not in line:
                continue
            key, value = line.split(";", 1)
            key = key.strip()
            value = value.strip()
            if key not in records:
                records[key] = value
    return records
