# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: CourseSchedule
import unittest


class TestCourse(unittest.TestCase):
    def test_create_course(self):
        c = Course("CS101", "Introduction to Programming", "Dr. Smith", 3)
        self.assertEqual(c.course_id, "CS101")
        self.assertEqual(c.course_name, "Introduction to Programming")
        self.assertEqual(c.instructor, "Dr. Smith")
        self.assertEqual(c.capacity, 3)

    def test_add_session(self):
        c = Course("CS101", "Intro", "Dr. Smith", 3)
        c.add_session(Session("Mon 10:00-11:00", "Room 101"))
        self.assertEqual(len(c.schedules), 1)
        self.assertEqual(c.schedules[0].day, "Mon 10:00-11:00")
        self.assertEqual(c.schedules[0].room, "Room 101")

    def test_add_instructor(self):
        c = Course("CS101", "Intro", "Dr. Smith", 3)
        c.add_instructor(Instructor("Dr. Smith", 20))
        self.assertEqual(len(c.instructors), 1)
        self.assertEqual(c.instructors[0].name, "Dr. Smith")
        self.assertEqual(c.instructors[0].experience, 20)

    def test_add_room(self):
        c = Course("CS101", "Intro", "Dr. Smith", 3)
        c.add_room(Room("Room 101", 50))
        self.assertEqual(len(c.rooms), 1)
        self.assertEqual(c.rooms[0].name, "Room 101")
        self.assertEqual(c.rooms[0].capacity, 50)

    def test_add_attendee(self):
        c = Course("CS101", "Intro", "Dr. Smith", 3)
        c.add_attendee(Attendee("Alice", 19))
        self.assertEqual(len(c.attendees), 1)
        self.assertEqual(c.attendees[0].name, "Alice")
        self.assertEqual(c.attendees[0].age, 19)


class TestScheduleApp(unittest.TestCase):
    def test_app_creation(self):
        app = ScheduleApp()
        self.assertIsNotNone(app)

    def test_add_course(self):
        app = ScheduleApp()
        app.add_course(Course("CS101", "Intro", "Dr. Smith", 3))
        self.assertEqual(len(app.courses), 1)
        self.assertEqual(app.courses[0].course_id, "CS101")

    def test_add_instructor(self):
        app = ScheduleApp()
        app.add_instructor(Instructor("Dr. Smith", 20))
        self.assertEqual(len(app.instructors), 1)
        self.assertEqual(app.instructors[0].name, "Dr. Smith")

    def test_add_room(self):
        app = ScheduleApp()
        app.add_room(Room("Room 101", 50))
        self.assertEqual(len(app.rooms), 1)
        self.assertEqual(app.rooms[0].name, "Room 101")

    def test_add_attendee(self):
        app = ScheduleApp()
        app.add_attendee(Attendee("Alice", 19))
        self.assertEqual(len(app.attendees), 1)
        self.assertEqual(app.attendees[0].name, "Alice")


if __name__ == "__main__":
    unittest.main()
