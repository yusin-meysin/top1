# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: CourseSchedule
def archive_records(records, cutoff_date=None):
    """Archive completed or old records."""
    if cutoff_date is None:
        cutoff_date = datetime(2024, 1, 1)
    archived = []
    for record in records:
        if isinstance(record, dict) and 'end_date' in record:
            end_date = record['end_date']
            if isinstance(end_date, str):
                end_date = datetime.strptime(end_date[:10], '%Y-%m-%d').date()
            elif isinstance(end_date, datetime):
                end_date = end_date.date()
            if end_date <= cutoff_date:
                archived.append(record)
        else:
            if not record.get('active', True):
                archived.append(record)
    return archived
