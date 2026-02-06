# Concrete Strategy
from typing import List
from strategy import TrainingStrategy


class HighIntensityStrategy(TrainingStrategy):
    def build_session(self, players: List[str]) -> str:
        return (
            f"High Intensity: sprint, pressing, small-sided games "
            f"({len(players)} pemain)"  # Latihan intens
        )


class RecoveryStrategy(TrainingStrategy):
    def build_session(self, players: List[str]) -> str:
        return (
            f"Recovery: stretching, ice bath, light jog "
            f"({len(players)} pemain)"  # Latihan pemulihan
        )


class EnduranceStrategy(TrainingStrategy):
    def build_session(self, players: List[str]) -> str:
        return (
            f"Endurance: long run, interval cardio "
            f"({len(players)} pemain)"  # Latihan fisik daya tahan
        )
