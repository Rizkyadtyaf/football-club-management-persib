from abc import ABC, abstractmethod  # Untuk interface/abstract class
from events import BaseEvent  # Tipe event dasar


class Observer(ABC):  # Interface untuk semua observer
    @abstractmethod
    def update(self, event: BaseEvent) -> None:  # Dipanggil saat ada event
        pass