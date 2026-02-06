from typing import List  # Untuk type hint list
from observer import Observer  # Observer interface
from events import BaseEvent  # Event dasar


class Subject:  # Subject (Observable)
    def __init__(self) -> None:
        self._observers: List[Observer] = []  # Menyimpan observer

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:  # Cegah duplikasi observer
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:  # Hapus observer tertentu
            self._observers.remove(observer)

    def notify(self, event: BaseEvent) -> None:
        for observer in list(self._observers):  # Kirim event ke semua observer
            observer.update(event)