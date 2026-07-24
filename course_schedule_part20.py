# === Stage 20: Добавь восстановление записей из архива ===
# Project: CourseSchedule
import zipfile, os, json

def load_from_archive(archive_path: str) -> list[dict]:
    """Восстанавливает записи из zip-архива и возвращает их как список словарей."""
    records = []
    if not os.path.exists(archive_path):
        return records
    with zipfile.ZipFile(archive_path, 'r') as zf:
        for name in zf.namelist():
            if name.endswith('.json'):
                raw = zf.read(name)
                try:
                    records.extend(json.loads(raw.decode('utf-8')))
                except Exception:
                    pass
    return records
