from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_player(self, player):
        pass
