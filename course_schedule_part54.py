# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: CourseSchedule
ЗАБР = {}

def add_favorite(course_id):
    if course_id in ЗАБР:
        return
    for cid, rec in ЗАБР.items():
        if cid == course_id:
            return
    ЗАБР[course_id] = course_id

def remove_favorite(course_id):
    ЗАБР.pop(course_id, None)

def list_favorites():
    if not ЗАБР:
        print("Избранных записей нет")
        return
    print("Избранные записи:")
    for cid in ЗАБР:
        print(cid)

def quick_access():
    if not ЗАБР:
        print("Сначала добавьте записи в избранное")
        return
    print("Быстрый доступ:")
    for cid in ЗАБР:
        print(cid)

def toggle_favorite(course_id):
    if course_id in ЗАБР:
        remove_favorite(course_id)
    else:
        add_favorite(course_id)
