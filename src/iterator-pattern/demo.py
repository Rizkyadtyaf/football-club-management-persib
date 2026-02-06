from persib_squad import PersibSquad
from player import Player


def print_player(p: Player) -> None:
    print(f"[PERSIB] #{p.number} {p.name} ({p.position}, {p.role})")  # Output rapi


def main() -> None:
    print("=== ITERATOR PATTERN - STUDI KASUS: PERSIB BANDUNG ===\n")

    squad = PersibSquad()  # Collection skuad Persib

    # Data dari halaman resmi Persib (club-players) :contentReference[oaicite:1]{index=1}
    # PENJAGA GAWANG
    squad.add_player(Player(1, "Adam J Przybek", "GK", "GK"))
    squad.add_player(Player(50, "Fitrah Maulana", "GK", "GK"))
    squad.add_player(Player(14, "Teja Paku Alam", "GK", "GK"))

    # PEMAIN BELAKANG (anggap role DEF, posisi disederhanakan jadi DF)
    squad.add_player(Player(44, "Dion W E Markx", "DF", "DEF"))
    squad.add_player(Player(3, "Layvin Kurzawa", "DF", "DEF"))
    squad.add_player(Player(66, "Kevin M.I Pasha", "DF", "DEF"))
    squad.add_player(Player(93, "Federico Barba", "DF", "DEF"))
    squad.add_player(Player(48, "Patricio M Matricardi", "DF", "DEF"))
    squad.add_player(Player(4, "Julio Cesar", "DF", "DEF"))
    squad.add_player(Player(19, "Alfeandra Dewangga S", "DF", "DEF"))
    squad.add_player(Player(16, "Achmad Jufriyanto", "DF", "DEF"))
    squad.add_player(Player(5, "Kakang Rudianto", "DF", "DEF"))
    squad.add_player(Player(6, "Robi Darwis", "DF", "DEF"))

    # GELANDANG (anggap role MID, posisi disederhanakan jadi MF)
    squad.add_player(Player(67, "Saddil Ramdani", "MF", "MID"))
    squad.add_player(Player(2, "Eliano Reijnders", "MF", "MID"))
    squad.add_player(Player(33, "Thom J.M Haye", "MF", "MID"))
    squad.add_player(Player(36, "Athaya Zahran", "MF", "MID"))
    squad.add_player(Player(55, "Frans Putros", "MF", "MID"))
    squad.add_player(Player(85, "Nazriel A Syahdan", "MF", "MID"))
    squad.add_player(Player(97, "Berguinho da Silva", "MF", "MID"))
    squad.add_player(Player(8, "Luciano Guaycochea", "MF", "MID"))
    squad.add_player(Player(18, "Adam Alis S", "MF", "MID"))
    squad.add_player(Player(7, "Beckham Putra N.", "MF", "MID"))
    squad.add_player(Player(13, "Febri Hariyadi", "MF", "MID"))
    squad.add_player(Player(23, "Marc A. Klok", "MF", "MID"))

    # PENYERANG (anggap role ATT, posisi disederhanakan jadi FW)
    squad.add_player(Player(90, "Andrew Jung", "FW", "ATT"))
    squad.add_player(Player(98, "Ramon Tangue", "FW", "ATT"))
    squad.add_player(Player(94, "Uilliam Barros P", "FW", "ATT"))
    squad.add_player(Player(73, "Zulkifli Lukmansyah", "FW", "ATT"))

    print("=== DAFTAR PEMAIN PERSIB (SEMUA) ===")
    for p in squad:  # Iterator default
        print_player(p)

    print("\n=== FILTER ROLE: DEFENDER (DEF) ===")
    for p in squad.iter_by_role("DEF"):  # Iterator filter role
        print_player(p)

    print("\n=== FILTER ROLE: MIDFIELDER (MID) ===")
    for p in squad.iter_by_role("MID"):
        print_player(p)

    print("\n=== FILTER ROLE: ATTACKER (ATT) ===")
    for p in squad.iter_by_role("ATT"):
        print_player(p)

    print("\n=== FILTER POSISI: GK ===")
    for p in squad.iter_by_position("GK"):  # Iterator filter posisi
        print_player(p)


if __name__ == "__main__":
    main()  # Entry point program
