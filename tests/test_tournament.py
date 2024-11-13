import unittest
from src.tournament import Tournament

class TestTournament(unittest.TestCase):
    def test_initialization(self):
        tournament = Tournament("Championship", 10000)
        self.assertEqual(tournament.name, "Championship")

if __name__ == "__main__":
    unittest.main()
