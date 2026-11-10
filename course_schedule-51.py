# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: CourseSchedule
class ChangeLog:
    def __init__(self):
        self._log = []
        self._lock = threading.Lock()

    def add(self, action, entity, detail, user="system"):
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "entity": entity,
            "detail": detail,
            "user": user,
        }
        with self._lock:
            self._log.append(entry)
        return entry

    def record(self, action, entity, detail, user="system"):
        return self.add(action, entity, detail, user)

    def get(self, limit=50, reverse=True):
        with self._lock:
            entries = list(self._log)
        if reverse:
            entries = entries[::-1]
        return entries[-limit:] if limit else entries

    def search(self, entity, keyword=None, limit=50):
        with self._lock:
            entries = list(self._log)
        result = [e for e in entries if e["entity"] == entity]
        if keyword:
            result = [e for e in result if keyword in e["detail"]]
        result = result[-limit:] if limit else result
        return result

    def clear(self):
        with self._lock:
            self._log.clear()

    def summary(self, entity=None):
        with self._lock:
            entries = list(self._log)
        if entity:
            entries = [e for e in entries if e["entity"] == entity]
        counts = {}
        for e in entries:
            key = (e["action"], e["entity"])
            counts[key] = counts.get(key, 0) + 1
        return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
