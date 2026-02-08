from player import Player
from decorators import Captain, Injured

if __name__ == "__main__":
    p = Player("Beckham Putra", "MF")
    print("Base:", p.profile(), "-", p.availability())

    p2 = Captain(p)
    p2 = Injured(p2)

    print("Decorated:", p2.profile(), "-", p2.availability())
