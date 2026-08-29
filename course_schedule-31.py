# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: CourseSchedule
def switch_profile():
    """Переключение активного пользовательского профиля."""
    active = get_active_profile()
    profiles = get_profiles()
    if not profiles:
        print("Нет профилей. Добавьте через add_profile()")
        return
    print(f"\n📋 Доступные профили:")
    for i, p in enumerate(profiles, 1):
        marker = " ✓" if p['id'] == active['id'] else ""
        print(f"  {i}. {p['name']}{marker}")
    try:
        choice = int(input("\nВыберите номер профиля (или Enter для текущего): "))
    except (ValueError, EOFError):
        return
    if choice == 0:
        return
    idx = choice - 1
    if 0 <= idx < len(profiles):
        new = profiles[idx]
        if new['id'] == active['id']:
            print("Вы уже на этом профиле.")
            return
        active = update_profile(active['id'], {'name': new['name']})
        if not active:
            print("Ошибка обновления профиля.")
            return
        print(f"\n✅ Переключено на профиль: {active['name']}")
        if active['is_admin']:
            print("👑 Вы стали администратором.")
        else:
            print("🎓 Вы стали студентом.")
    else:
        print("Неверный выбор.")
