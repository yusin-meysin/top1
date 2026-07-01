# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: CourseSchedule
def sort_records(records, key='date', reverse=False):
    if key == 'name':
        return sorted(records, key=lambda r: (r['course'].lower(), r.get('priority', 0)), reverse=reverse)
    elif key == 'priority':
        return sorted(records, key=lambda r: (-int(r.get('priority', 0)), r['date']), reverse=False)
    else: # date or default
        def sort_key(rec):
            try:
                d = rec['date'].split()
                if len(d) == 2:
                    return (d[1], int(d[0].replace('ч', '')), rec.get('priority', 0))
                else:
                    return (rec['date'], 0, rec.get('priority', 0))
            except Exception:
                return (str(rec['date']), 0, rec.get('priority', 0))
        return sorted(records, key=sort_key, reverse=False)
