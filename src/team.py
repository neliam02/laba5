class Team:
    def __init__(self, name):
        self.name = name
        self.members = []  # Це список для збереження членів команди

    def recruitMember(self, member):
        """
        Додає нового члена до команди.
        :param member: Член команди (Player, Coach, Staff)
        """
        self.members.append(member)
        print(f"{member.name} приєднався до команди {self.name}.")

    def remove_member(self, member):
        """
        Видаляє члена з команди.
        :param member: Член команди для видалення
        """
        if member in self.members:
            self.members.remove(member)
            print(f"{member.name} покинув команду {self.name}.")
        else:
            print(f"{member.name} не є членом команди {self.name}.")

    def get_members(self):
        """
        Повертає список членів команди.
        """
        return self.members
