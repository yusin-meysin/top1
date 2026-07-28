# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: CourseSchedule
def print_schedule_table(schedule):
    """Выводит расписание в виде форматированной таблицы."""
    if not schedule:
        print("Расписание пусто.")
        return
    
    # Заголовки столбцов
    headers = ["Курс", "Преподаватель", "День", "Время", "Аудитория"]
    
    # Вычисляем ширину каждого столбца
    col_widths = [len(h) for h in headers]
    
    rows_data = []
    for course, teacher, day, time_slot, room in schedule:
        row = [course.name, teacher, day, time_slot, room]
        rows_data.append(row)
        
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
    
    # Формируем строку с разделителями
    separator_line = "─" * sum(col_widths) + "─"
    
    print(separator_line)
    header_row = " │ ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_row)
    print(separator_line)
    
    # Вывод данных
    for row in rows_data:
        data_row = " │ ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(data_row)
    
    print(separator_line)

# Пример использования (если файл запускается напрямую):
if __name__ == "__main__":
    # Создадим тестовые данные для проверки таблицы
    test_schedule = [
        ("Python Basics", "Иван Иванов", "Понедельник", "09:00-10:30", "Аудитория 1"),
        ("Java Advanced", "Петр Петров", "Среда", "14:00-15:30", "Аудитория 2"),
        ("Web Development", "Мария Сидорова", "Пятница", "10:00-11:30", "Аудитория 3"),
    ]
    
    print_schedule_table(test_schedule)
