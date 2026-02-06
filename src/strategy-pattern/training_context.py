from typing import List
from strategy import TrainingStrategy


class TrainingContext:
    def __init__(self, strategy: TrainingStrategy) -> None:
        self._strategy = strategy  # Strategi aktif

    def set_strategy(self, strategy: TrainingStrategy) -> None:
        self._strategy = strategy  # Ganti strategi tanpa ubah class lain

    def run_session(self, players: List[str]) -> None:
        plan = self._strategy.build_session(players)  # Delegasi ke strategi
        print(f"[SESI LATIHAN] {plan}")  # Tampilkan rencana latihan
