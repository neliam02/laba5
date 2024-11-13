import unittest
from src.training_program import TrainingProgram

class TestTrainingProgram(unittest.TestCase):
    def test_initialization(self):
        program = TrainingProgram("Strength Training", 4)
        self.assertEqual(program.name, "Strength Training")
        self.assertEqual(program.duration, 4)

if __name__ == "__main__":
    unittest.main()
