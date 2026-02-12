from abc import ABC, abstractmethod

class PlayerPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass
