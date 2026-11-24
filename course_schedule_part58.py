# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: CourseSchedule
class SimpleListView:
    def __init__(self, items=None):
        self._items = list(items) if items else []

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        if item in self._items:
            self._items.remove(item)

    def clear(self):
        self._items.clear()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"SimpleListView({self._items!r})"

    def get_all(self):
        return list(self._items)

    def get_item(self, index):
        return self._items[index]

    def contains(self, item):
        return item in self._items

    def count(self, predicate=None):
        if predicate is None:
            return len(self._items)
        return sum(1 for i in self._items if predicate(i))
