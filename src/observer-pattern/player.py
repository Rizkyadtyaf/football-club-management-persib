from datetime import datetime  # Untuk waktu event
from subject import Subject  # Subject base
from events import PlayerStatusChangedEvent  # Event status pemain


class Player(Subject):  # Player sebagai Subject
    def __init__(self, name: str, status: str = "FIT") -> None:
        super().__init__()
        self._name = name
        self._status = status

    def change_status(self, new_status: str) -> None:
        if new_status == self._status:  # Tidak kirim event jika status sama
            return

        old_status = self._status
        self._status = new_status

        event = PlayerStatusChangedEvent(  # Buat event perubahan status
            occurred_at=datetime.now(),
            player_name=self._name,
            old_status=old_status,
            new_status=new_status,
        )
        self.notify(event)  # Beri tahu semua observer