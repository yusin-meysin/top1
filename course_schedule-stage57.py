# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: CourseSchedule
def delete_courses_confirm(names, delete_all=False):
    if not names:
        print("Нет курсов для удаления.")
        return
    to_delete = names if delete_all else [n for n in names if n in COURSES and not COURSES[n]["active"]]
    if not to_delete:
        print("Курсы не найдены или активны.")
        return
    for name in to_delete:
        COURSES[name]["active"] = False
        print(f"Отмечен к удалению: {name}")
    if delete_all:
        for name in to_delete:
            del COURSES[name]
            print(f"Удалён полностью: {name}")
    print("Проверьте журнал посещаемости перед окончательным удалением.")
