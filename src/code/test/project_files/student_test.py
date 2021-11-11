import unittest
from student import Student

class TestStudentMethods(unittest.TestCase):

    def test_no_dropped_classes(self):

        test = Student()
        test.add_classes([1,2,3,4],[1,2,3,4])
        self.assertEqual(test.calculate_dropped_classes(), 0)

    def test_dropped_classes(self):
        test = Student()
        test.add_classes([1,2,3,4,5,6],[1,2,3,4])
        self.assertEqual(test.calculate_dropped_classes(), 2)

    def test_extra_registered_classes(self):
        test = Student()
        test.add_classes([1,2,3,4],[1,2,3,4,5,6])
        self.assertEqual(test.calculate_dropped_classes(), 0)

if __name__ == "__main__":
    unittest.main()
