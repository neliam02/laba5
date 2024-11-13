from .team_member import TeamMember

class Staff(TeamMember):
    def __init__(self, name, experience, role):
        super().__init__(name, experience)
        self.role = role

    def get_role(self):
        return "Staff"
