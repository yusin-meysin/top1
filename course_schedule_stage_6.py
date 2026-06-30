# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: CourseSchedule
class CourseScheduleFilter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status):
        return [r for r in self.records if r.get('status') == status]
    
    def filter_by_category(self, category):
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tags(self, tags):
        if not tags:
            return self.records.copy()
        tag_set = set(tags)
        return [r for r in self.records 
                if any(tag in r.get('tags', []) for tag in tag_set)]
    
    def combine_filters(self, status=None, category=None, tags=None):
        filtered = self.records
        if status:
            filtered = self.filter_by_status(status)
        if category:
            filtered = [r for r in filtered if r.get('category') == category]
        if tags:
            filtered = self.filter_by_tags(tags)
        return filtered
