from abc import ABC, abstractmethod

class TeamMember(ABC):
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    @abstractmethod
    def get_role(self):
        pass
