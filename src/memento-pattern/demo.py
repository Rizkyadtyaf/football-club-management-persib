from player import Player
from caretaker import Caretaker


def main():
    print("===== MEMENTO PATTERN (VERSI KOMPLEKS) =====")

    player = Player("Beckham Putra")
    caretaker = Caretaker()

    player.set_state("Top Form", 100)
    caretaker.add(player.save())

    player.set_state("Cedera", 60)
    caretaker.add(player.save())

    print("Rollback ke kondisi awal:")
    player.restore(caretaker.get(0))


if __name__ == "__main__":
    main()
