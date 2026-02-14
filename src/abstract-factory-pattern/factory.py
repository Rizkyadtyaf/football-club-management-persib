from abc import ABC, abstractmethod
from player import Player
from coach import Coach

class ClubFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass

    @abstractmethod
    def create_coach(self):
        pass


class PersibFactory(ClubFactory):
    def create_player(self):
        return Player()

    def create_coach(self):
        return Coach()
