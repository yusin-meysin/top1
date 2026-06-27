# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: CourseSchedule
def edit_record(record_id, updates):
    if record_id not in records:
        raise ValueError(f"Record with id {record_id} not found")
    for key, value in updates.items():
        if hasattr(records[record_id], key):
            setattr(records[record_id], key, value)
        else:
            raise AttributeError(f"Field '{key}' does not exist on record type {type(records[record_id]).__name__}")
