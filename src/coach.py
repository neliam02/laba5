from .team_member import TeamMember

class Coach(TeamMember):
    def __init__(self, name, experience, style):
        super().__init__(name, experience)
        self.style = style

    def get_role(self):
        return "Coach"
