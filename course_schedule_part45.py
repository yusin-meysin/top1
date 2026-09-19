# === Stage 45: Добавь восстановление из резервной копии ===
# Project: CourseSchedule
def load_backup(backup_path):
    """Восстанавливает все данные из JSON-резервной копии."""
    import json
    with open(backup_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key in ['courses', 'lectures', 'instructors', 'rooms', 'attendance']:
        setattr(CourseSchedule, key, data.get(key, []))
    print(f"Backup restored from {backup_path}: {len(CourseSchedule.courses)} courses, {len(CourseSchedule.lectures)} lectures, {len(CourseSchedule.instructors)} instructors, {len(CourseSchedule.rooms)} rooms")

if __name__ == '__main__':
    backup_file = 'backup.json'
    if not backup_file:
        backup_file = input("Enter backup file path (default: backup.json): ").strip() or 'backup.json'
    try:
        load_backup(backup_file)
    except FileNotFoundError:
        print(f"Backup file '{backup_file}' not found. Creating a new schedule from scratch.")
    except json.JSONDecodeError:
        print(f"Invalid backup file '{backup_file}'. Please check the file.")
