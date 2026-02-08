from mediator import TeamMediator
from member import TeamMember


def main():
    print("===== MEDIATOR PATTERN =====")

    mediator = TeamMediator()

    coach = TeamMember("Bojan Hodak", "Pelatih", mediator)
    doctor = TeamMember("Dokter Asep", "Dokter Tim", mediator)
    manager = TeamMember("Umuh Muchtar", "Manajer Tim", mediator)
    player = TeamMember("Beckham Putra", "Pemain", mediator)

    coach.send("Intensitas latihan diturunkan hari ini")


if __name__ == "__main__":
    main()
