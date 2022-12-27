import unittest
from datetime import timedelta
from student import Student
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def test_full_name(self):
        print("test_full_name")

        self.assertEqual(self.student.ful_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")

        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        current_end_date = self.student.end_date
        self.student.apply_extension(50)

        self.assertEqual(self.student.end_date, current_end_date + timedelta(days=50))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

    def tearDown(self) -> None:
        print("tearDown")


if __name__ == "__main__":
    unittest.main()