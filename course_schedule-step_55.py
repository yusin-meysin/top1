# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: CourseSchedule
def soft_duplicate_check(records, key_fn, warn=True):
    seen = {}
    for rec in records:
        k = key_fn(rec)
        if k in seen:
            if warn:
                print(f"Возможно, дубликат записи: {rec!r} (ключ {k})")
        else:
            seen[k] = rec
    return seen
