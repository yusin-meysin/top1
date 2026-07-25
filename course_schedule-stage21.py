# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: CourseSchedule
class Reminder:
    def __init__(self, title, description="", due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
    
    def is_overdue(self):
        if not self.due_date or self.due_date < datetime.now().date():
            return True
        return False
    
    def __repr__(self):
        status = "overdue" if self.is_overdue() else f"due on {self.due_date}"
        return f"<Reminder '{self.title}' [{status}]>"

class ReminderManager:
    def __init__(self):
        self._reminders = []
    
    def add_reminder(self, reminder):
        self._reminders.append(reminder)
        print(f"Added reminder: {reminder}")
    
    def remove_reminder(self, reminder):
        removed = False
        for i in range(len(self._reminders)):
            if self._reminders[i] == reminder:
                self._reminders.pop(i)
                removed = True
                break
        if not removed:
            print("Reminder not found")
    
    def get_overdue_reminders(self):
        return [r for r in self._reminders if r.is_overdue()]
    
    def list_all(self):
        return self._reminders.copy()

# Example usage
if __name__ == "__main__":
    mgr = ReminderManager()
    mgr.add_reminder(Reminder("Grade papers", due_date=datetime.now().date()))
    print(mgr.get_overdue_reminders())
