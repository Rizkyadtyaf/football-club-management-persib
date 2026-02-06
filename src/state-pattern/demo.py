from player_context import Player


def main() -> None:
    positions = [
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

    players = [Player(pos) for pos in positions]  # Buat object Player untuk 11 posisi

    print("=== STATUS AWAL TIM (11 PEMAIN) ===")
    for p in players:
        p.summary()  # Semua default FIT

    print("\n=== SIMULASI TRANSISI STATE (CONTOH 3 POSISI) ===")

    cm = players[5]  # CM
    cm.injury()  # CM cedera
    cm.summary()
    cm.recover()  # CM masuk recovery
    cm.summary()
    cm.recover()  # CM pulih total jadi FIT
    cm.summary()

    cb = players[2]  # CB
    cb.suspend()  # CB kena sanksi
    cb.summary()

    st = players[10]  # ST
    st.injury()  # ST cedera
    st.summary()


if __name__ == "__main__":
    main()  # Entry point program
