import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_initialization(self):
        player = Player("Alice", 5, ["Dribbling", "Passing"])
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.experience, 5)
        self.assertEqual(player.skills, ["Dribbling", "Passing"])
    
    def test_get_role(self):
        player = Player("Alice", 5, ["Dribbling", "Passing"])
        self.assertEqual(player.get_role(), "Player")
    
    def test_display_skills(self):
        player = Player("Alice", 5, ["Dribbling", "Passing"])
        self.assertEqual(player.display_skills(), "Alice має наступні навички: Dribbling, Passing")

if __name__ == "__main__":
    unittest.main()
