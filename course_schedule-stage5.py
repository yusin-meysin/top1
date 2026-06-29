# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: CourseSchedule
def delete_record(entity_type, record_id):
    if entity_type not in db:
        print(f"Ошибка: тип сущности '{entity_type}' не найден.")
        return False
    records = db[entity_type]
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} для типа '{entity_type}' не найдена.")
        return False
    del records[record_id]
    print(f"Запись успешно удалена: {entity_type} #{record_id}")
    return True

def handle_missing_ids(entity_type, missing_ids):
    if not missing_ids:
        return
    for mid in missing_ids:
        if entity_type in db and mid in db[entity_type]:
            del db[entity_type][mid]
        print(f"Удалена отсутствующая запись (возможно, уже была удалена или не существовала): {entity_type} #{mid}")
