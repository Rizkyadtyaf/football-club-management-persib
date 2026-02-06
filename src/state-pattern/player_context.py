from state import PlayerState
from states import FitState


class Player:
    def __init__(self, position: str) -> None:
        self._position = position  # Posisi pemain (GK/CB/ST/dll)
        self._state: PlayerState = FitState()  # State awal: FIT

    def status(self) -> str:
        return self._state.name()  # Ambil nama state

    def can_train(self) -> bool:
        return self._state.can_train()  # Delegasi ke state aktif

    def injury(self) -> None:
        self._state = self._state.on_injury()  # Transisi saat cedera

    def recover(self) -> None:
        self._state = self._state.on_recover()  # Transisi saat pemulihan

    def suspend(self) -> None:
        self._state = self._state.on_suspend()  # Transisi saat kena sanksi

    def summary(self) -> None:
        izin = "BOLEH" if self.can_train() else "TIDAK BOLEH"  # Izin latihan berdasarkan state
        print(f"[PERSIB] {self._position} | status={self.status()} | latihan={izin}")  # Ringkasan
