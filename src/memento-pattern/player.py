from memento import PlayerMemento


class Player:
    def __init__(self, name):
        self.name = name
        self.condition = "Fit"
        self.fitness = 100

    def set_state(self, condition, fitness):
        self.condition = condition
        self.fitness = fitness
        print(f"{self.name} | Kondisi: {condition}, Fitness: {fitness}")

    def save(self):
        return PlayerMemento(self.condition, self.fitness)

    def restore(self, memento: PlayerMemento):
        self.condition = memento.condition
        self.fitness = memento.fitness
        print(f"{self.name} dikembalikan ke kondisi terbaik")
