# === Stage 32: Добавь журнал действий пользователя ===
# Project: CourseSchedule
import json

class ActionLog:
    def __init__(self):
        self.actions = []

    def log(self, action_type, description):
        self.actions.append({"type": action_type, "description": description})

    def get_log(self):
        return self.actions

    def clear_log(self):
        self.actions = []

    def print_log(self, max_entries=10):
        log = self.get_log()
        if not log:
            print("\n[Журнал действий] - пусто.")
            return
        print(f"\n[Журнал действий] (последние {min(len(log), max_entries)} записей):")
        for i, entry in enumerate(log[-max_entries:], 1):
            print(f"  {i}. [{entry['type']}] {entry['description']}")

log = ActionLog()
