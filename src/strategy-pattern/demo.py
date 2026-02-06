from training_context import TrainingContext
from strategies import HighIntensityStrategy, RecoveryStrategy, EnduranceStrategy


def main() -> None:
    print("=== STRATEGY PATTERN - STUDI KASUS: PERSIB BANDUNG ===")
    players = [
        "GK",  # Goalkeeper
        "LB",  # Left Back
        "CB",  # Center Back
        "RB",  # Right Back
        "DM",  # Defensive Midfielder
        "CM",  # Central Midfielder
        "AM",  # Attacking Midfielder
        "LW",  # Left Wing
        "RW",  # Right Wing
        "CF",  # Center Forward
        "ST",  # Striker 
    ]

    context = TrainingContext(HighIntensityStrategy())  # Strategi awal: intens
    context.run_session(players)

    context.set_strategy(RecoveryStrategy())  # Ganti ke strategi pemulihan
    context.run_session(players)

    context.set_strategy(EnduranceStrategy())  # Ganti ke strategi daya tahan
    context.run_session(players)


if __name__ == "__main__":
    main()  # Entry point program
