# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: CourseSchedule
import copy

def dry_run(operation, data, **kwargs):
    state = copy.deepcopy(data)
    try:
        state = operation(state, **kwargs)
        return state
    except Exception as e:
        raise e
