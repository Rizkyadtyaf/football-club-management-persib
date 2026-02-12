class Player:
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals

    def accept(self, visitor):
        visitor.visit_player(self)
