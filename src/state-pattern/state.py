# state.py
# Berisi definisi abstract state (kontrak).
# Semua concrete state harus mengimplementasikan perilaku dan transisi di sini.

from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def name(self) -> str:  # Nama state untuk ditampilkan
        pass

    @abstractmethod
    def can_train(self) -> bool:  # Apakah boleh latihan?
        pass

    @abstractmethod
    def on_injury(self) -> "PlayerState":  # Transisi saat cedera
        pass

    @abstractmethod
    def on_recover(self) -> "PlayerState":  # Transisi saat pemulihan
        pass

    @abstractmethod
    def on_suspend(self) -> "PlayerState":  # Transisi saat kena sanksi
        pass
