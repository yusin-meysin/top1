# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: CourseSchedule
import os, json, datetime

def backup_data_file(data_file_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    base, ext = os.path.splitext(data_file_path)
    backup_name = f"{base}.backup_{datetime.datetime.now():%Y%m%d_%H%M%S}{ext}"
    backup_path = os.path.join(backup_dir, backup_name)
    with open(data_file_path, 'r', encoding='utf-8') as src, open(backup_path, 'w', encoding='utf-8') as dst:
        dst.write(src.read())
    return backup_path

def restore_data_file(backup_path, data_file_path):
    with open(backup_path, 'r', encoding='utf-8') as src, open(data_file_path, 'w', encoding='utf-8') as dst:
        dst.write(src.read())
    return data_file_path
