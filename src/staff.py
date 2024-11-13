from .team_member import TeamMember

class Staff(TeamMember):
    def __init__(self, name, experience, specialty):
        super().__init__(name, experience)
        self.specialty = specialty

    def get_role(self):
        return "Staff"
