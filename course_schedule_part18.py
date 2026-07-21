# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: CourseSchedule
class Tag:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tag name must be a non-empty string")
        self.name = name.strip().lower()

    def __repr__(self):
        return f"Tag({self.name!r})"


class Course:
    def add_tag(self, tag):
        if isinstance(tag, str):
            tag = Tag(tag)
        elif not isinstance(tag, Tag):
            raise TypeError("tag must be a string or Tag instance")
        if self._tags is None:
            from collections import defaultdict
            self._tags = defaultdict(set)
        tag_name = tag.name
        if tag_name in self._tags[tag]:
            return False  # already present
        self._tags[tag].add(tag_name)
        return True

    def remove_tag(self, tag):
        if isinstance(tag, str):
            tag = Tag(tag)
        elif not isinstance(tag, Tag):
            raise TypeError("tag must be a string or Tag instance")
        if self._tags is None:
            return False
        tag_name = tag.name
        if tag_name in self._tags[tag]:
            self._tags[tag].discard(tag_name)
            return True
        return False
