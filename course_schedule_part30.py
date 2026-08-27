# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: CourseSchedule
class UserProfile:
    def __init__(self, name, role, schedule=None):
        self.name = name
        self.role = role  # 'student', 'lecturer', 'admin'
        self.schedule = schedule or []
    
    def add_event(self, event):
        self.schedule.append(event)
    
    def get_events(self):
        return self.schedule
    
    def __repr__(self):
        return f"UserProfile(name='{self.name}', role='{self.role}')"

# Пример использования нескольких профилей
profiles = {
    "student1": UserProfile("Иван Иванов", "student"),
    "lecturer1": UserProfile("Петр Петров", "lecturer"),
    "admin1": UserProfile("Анна Сидорова", "admin"),
}
