class Caretaker:
    def __init__(self):
        self.history = []

    def add(self, memento):
        self.history.append(memento)

    def get(self, index):
        return self.history[index]
