# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: CourseSchedule
class RollbackException(Exception):
    """
    Raised when a requested action cannot be rolled back.
    Used when the system is in a state where undo is logically impossible,
    e.g., when the schedule has not been saved to a history file yet,
    or when a rollback would leave the system in an inconsistent state.
    """
    def __init__(self, message: str, action: str):
        super().__init__(f"Cannot roll back action '{action}': {message}")
        self.action = action
        self.message = message

    def __str__(self) -> str:
        return f"RollbackException(action='{self.action}', message='{self.message}')"
