# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: CourseSchedule
APP_CONFIG = {
    "app_name": "CourseSchedule",
    "version": "0.1.0",
    "schedule_year": 2024,
    "default_room_capacity": 30,
    "max_teachers": 5,
    "max_rooms": 10,
    "max_students_per_class": 100,
    "working_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "working_hours_start": 8,
    "working_hours_end": 18,
    "lecture_duration_min": 90,
    "practical_duration_min": 60,
    "semester_start": "September",
    "semester_end": "May",
    "attendance_threshold": 75,
    "log_level": "INFO",
    "database_path": None,
    "log_file": "logs/app.log",
    "debug_mode": False,
}
