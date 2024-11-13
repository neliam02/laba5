# player.py
from .team_member import TeamMember

class Player(TeamMember):
    def __init__(self, name, experience, skills):
        """Ініціалізація гравця з ім'ям, досвідом та навичками"""
        super().__init__(name, experience)  # Викликаємо конструктор батьківського класу
        self.skills = skills  # Навички гравця
    
    def get_role(self):
        """Повертає роль гравця"""
        return "Player"
    
    def display_skills(self):
        """Метод для відображення навичок гравця"""
        return f"{self.name} має наступні навички: {', '.join(self.skills)}"
