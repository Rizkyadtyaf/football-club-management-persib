class TeamMember:
    def __init__(self, name, role, mediator):
        self.name = name
        self.role = role
        self.mediator = mediator
        mediator.add_member(self)

    def send(self, message):
        print(f"[{self.role}] {self.name} mengirim: {message}")
        self.mediator.notify(message, self)

    def receive(self, message):
        print(f"[{self.role}] {self.name} menerima: {message}")
