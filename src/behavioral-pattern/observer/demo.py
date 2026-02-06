from datetime import datetime  # Wajib: dipakai untuk datetime.now()
from player import Player
from subject import Subject
from events import TrainingScheduleChangedEvent
from notifiers import CoachNotifier, ManagerNotifier, MedicalStaffNotifier


class TrainingSchedule(Subject):  # Subject untuk jadwal latihan
    def __init__(self, date: str, time: str, location: str) -> None:
        super().__init__()
        self._date = date
        self._time = time
        self._location = location

    def change_schedule(self, new_time: str, new_location: str) -> None:
        event = TrainingScheduleChangedEvent(  # Buat event perubahan jadwal
            occurred_at=datetime.now(),
            date=self._date,
            old_time=self._time,
            new_time=new_time,
            location=new_location
        )
        self._time = new_time
        self._location = new_location
        self.notify(event)  # Kirim event ke observer


def main() -> None:
    coach = CoachNotifier()  # Observer pelatih
    manager = ManagerNotifier()  # Observer manajer
    medic = MedicalStaffNotifier()  # Observer medis

    player = Player("Pemain Utama")  # Subject player
    player.attach(coach)
    player.attach(manager)
    player.attach(medic)

    print("=== STATUS PEMAIN ===")
    player.change_status("INJURED")
    player.change_status("FIT")

    print("\n=== JADWAL LATIHAN ===")
    training = TrainingSchedule("2026-02-06", "07:00", "Sidolig")
    training.attach(coach)
    training.attach(manager)
    training.change_schedule("16:00", "GBLA")


if __name__ == "__main__":  # Biar main() kepanggil saat run demo.py
    main()
