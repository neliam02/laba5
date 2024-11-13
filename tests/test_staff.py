import unittest
from src.staff import Staff

class TestStaff(unittest.TestCase):
    def test_initialization(self):
        staff = Staff("Carol", 3, "Analyst")
        self.assertEqual(staff.name, "Carol")
        self.assertEqual(staff.experience, 3)
        self.assertEqual(staff.role, "Analyst")
    
    def test_get_role(self):
        staff = Staff("Carol", 3, "Analyst")
        self.assertEqual(staff.get_role(), "Staff")

if __name__ == "__main__":
    unittest.main()
