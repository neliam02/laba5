from .team_member import TeamMember

class Coach(TeamMember):
    def __init__(self, name, experience, specialization):
        super().__init__(name, experience)
        self.specialization = specialization

    def get_role(self):
        return "Coach"
