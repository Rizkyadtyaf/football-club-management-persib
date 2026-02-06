# states.py
# Berisi implementasi concrete state (FIT, INJURED, RECOVERY, SUSPENDED).
# Setiap state menentukan perilaku dan transisi state pemain.

from state import PlayerState


class FitState(PlayerState):
    def name(self) -> str:
        return "FIT"  # Siap latihan/bertanding

    def can_train(self) -> bool:
        return True  # Boleh latihan penuh

    def on_injury(self) -> PlayerState:
        return InjuredState()  # FIT -> INJURED

    def on_recover(self) -> PlayerState:
        return self  # FIT tetap FIT

    def on_suspend(self) -> PlayerState:
        return SuspendedState()  # FIT -> SUSPENDED


class InjuredState(PlayerState):
    def name(self) -> str:
        return "INJURED"  # Cedera

    def can_train(self) -> bool:
        return False  # Tidak boleh latihan normal

    def on_injury(self) -> PlayerState:
        return self  # Tetap INJURED

    def on_recover(self) -> PlayerState:
        return RecoveryState()  # INJURED -> RECOVERY

    def on_suspend(self) -> PlayerState:
        return self  # Cedera tidak berubah jadi suspend


class RecoveryState(PlayerState):
    def name(self) -> str:
        return "RECOVERY"  # Pemulihan

    def can_train(self) -> bool:
        return True  # Boleh latihan ringan

    def on_injury(self) -> PlayerState:
        return InjuredState()  # RECOVERY -> INJURED (kambuh)

    def on_recover(self) -> PlayerState:
        return FitState()  # RECOVERY -> FIT

    def on_suspend(self) -> PlayerState:
        return SuspendedState()  # RECOVERY -> SUSPENDED


class SuspendedState(PlayerState):
    def name(self) -> str:
        return "SUSPENDED"  # Sanksi/akumulasi kartu

    def can_train(self) -> bool:
        return True  # Boleh latihan, tapi tidak bisa main

    def on_injury(self) -> PlayerState:
        return InjuredState()  # SUSPENDED -> INJURED

    def on_recover(self) -> PlayerState:
        return self  # Suspend tidak hilang karena recover

    def on_suspend(self) -> PlayerState:
        return self  # Tetap SUSPENDED
