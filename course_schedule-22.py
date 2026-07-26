# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: CourseSchedule
def check_overdue_reminders():
    """Проверяет напоминания, срок которых истёк, и выводит список."""
    overdue = []
    for reminder in reminders:
        if reminder['status'] == 'pending' and datetime.now() > reminder['date']:
            overdue.append(reminder)
    return overdue

# Пример использования:
# overdue_reminders = check_overdue_reminders()
# print(f"Просрочено напоминаний: {len(overdue_reminders)}")
