# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: CourseSchedule
def weekly_stats_by_dates(schedule):
    """Calculate weekly statistics grouped by week dates."""
    stats = {}
    for entry in schedule:
        if not hasattr(entry, 'date'):
            continue
        week_start = entry.date.replace(day=1)
        week_end = (week_start + timedelta(weeks=1)).replace(day=28)
        key = week_end.strftime('%Y-%m-%d')
        if key not in stats:
            stats[key] = {'days': [], 'total_hours': 0, 'count': 0}
        stats[key]['days'].append(entry.date)
        stats[key]['total_hours'] += getattr(entry, 'hours', 1)
        stats[key]['count'] += 1
    return stats
