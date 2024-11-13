import unittest
from src.team import Team
from src.player import Player

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Dream Team")
        self.player1 = Player("John Doe", "Advanced", ["Passing", "Shooting"])
        self.player2 = Player("Jane Doe", "Beginner", ["Defense"])
    
    def test_recruit_member(self):
        """Тестуємо метод recruitMember"""
        self.team.recruitMember(self.player1)
        self.assertIn(self.player1, self.team.get_members())

    def test_remove_member(self):
        """Тестуємо метод remove_member"""
        self.team.recruitMember(self.player1)
        self.team.remove_member(self.player1)
        self.assertNotIn(self.player1, self.team.get_members())