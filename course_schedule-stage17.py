# === Stage 17: Добавь группировку записей по категориям ===
# Project: CourseSchedule
def group_by_category(self, records):
        grouped = {}
        for record in records:
            cat = record.get("category", "uncategorized")
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append(record)
        return dict(sorted(grouped.items()))
