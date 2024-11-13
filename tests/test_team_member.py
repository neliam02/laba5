import unittest
from src.player import Player

class TestTeamMember(unittest.TestCase):
    def test_initialization(self):
        member = Player("John", 3, ["Passing"])
        self.assertEqual(member.name, "John")
        self.assertEqual(member.experience, 3)

    def test_get_role(self):
        member = Player("John", 3, ["Passing"])
        self.assertEqual(member.get_role(), "Player")
