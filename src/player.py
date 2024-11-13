from .team_member import TeamMember

class Player(TeamMember):
    def __init__(self, name, experience, skills):
        super().__init__(name, experience)
        self.skills = skills

    def get_role(self):
        return "Player"
