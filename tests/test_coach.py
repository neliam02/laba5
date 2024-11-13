import unittest
from src.coach import Coach

class TestCoach(unittest.TestCase):
    def test_initialization(self):
        coach = Coach("Bob", 10, "Strategy")
        self.assertEqual(coach.name, "Bob")
        self.assertEqual(coach.experience, 10)
        self.assertEqual(coach.specialization, "Strategy")
    
    def test_get_role(self):
        coach = Coach("Bob", 10, "Strategy")
        self.assertEqual(coach.get_role(), "Coach")

if __name__ == "__main__":
    unittest.main()
