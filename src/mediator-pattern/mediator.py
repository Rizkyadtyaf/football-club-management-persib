class TeamMediator:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def notify(self, message, sender):
        for member in self.members:
            if member != sender:
                member.receive(message)
