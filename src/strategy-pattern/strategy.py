# Interface Strategy
from abc import ABC, abstractmethod
from typing import List


class TrainingStrategy(ABC):
    @abstractmethod
    def build_session(self, players: List[str]) -> str:  # Kontrak strategi latihan
        pass