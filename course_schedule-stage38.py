# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: CourseSchedule
def test_edge_cases():
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).title == 'CS101'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).day == '9'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).start == 10
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).end == 12

    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).title == 'CS101'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).day == '9'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).start == 10
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).end == 12

    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).title == 'CS101'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).day == '9'
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).start == 10
    assert Course('CS101', 'Python', 'Room A', 2024, 9, 10, 11, 11, 12).end == 12
