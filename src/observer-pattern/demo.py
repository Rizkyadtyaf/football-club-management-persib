from datetime import datetime  # Wajib: dipakai untuk datetime.now()
from player import Player  # Subject: pemain
from subject import Subject  # Subject base (Observable)
from events import TrainingScheduleChangedEvent  # Event perubahan jadwal
from notifiers import CoachNotifier, ManagerNotifier, MedicalStaffNotifier  # Observer


class TrainingSchedule(Subject):  # Subject untuk jadwal latihan
    def __init__(self, date: str, time: str, location: str) -> None:
        super().__init__()  # Init list observer
        self._date = date  # Tanggal latihan
        self._time = time  # Jam latihan
        self._location = location  # Lokasi latihan

    def change_schedule(self, new_time: str, new_location: str) -> None:
        event = TrainingScheduleChangedEvent(  # Buat event perubahan jadwal
            occurred_at=datetime.now(),  # Waktu perubahan terjadi
            date=self._date,  # Tanggal latihan
            old_time=self._time,  # Jam lama
            new_time=new_time,  # Jam baru
            location=new_location  # Lokasi baru
        )
        self._time = new_time  # Update jam
        self._location = new_location  # Update lokasi
        self.notify(event)  # Kirim event ke observer


def main() -> None:
    print("=== OBSERVER PATTERN - STUDI KASUS: PERSIB BANDUNG ===")  # Judul konteks

    coach = CoachNotifier()  # Observer: pelatih
    manager = ManagerNotifier()  # Observer: manajer tim
    medic = MedicalStaffNotifier()  # Observer: tim medis

    player = Player("ST")  # Contoh pemain (posisi) untuk studi kasus Persib Bandung
    player.attach(coach)  # Pelatih langganan notifikasi
    player.attach(manager)  # Manajer langganan notifikasi
    player.attach(medic)  # Tim medis langganan notifikasi

    print("\n=== EVENT OBSERVER: PERUBAHAN STATUS PEMAIN PERSIB BANDUNG ===")  # Bagian status pemain
    player.change_status("INJURED")  # Status berubah -> observer dapat notifikasi
    player.change_status("FIT")  # Status kembali fit -> observer dapat notifikasi

    print("\n=== JADWAL LATIHAN PERSIB BANDUNG ===")  # Bagian jadwal latihan
    training = TrainingSchedule("2026-02-06", "07:00", "Sidolig")  # Contoh lokasi Persib
    training.attach(coach)  # Pelatih ikut update jadwal
    training.attach(manager)  # Manajer ikut update jadwal
    training.change_schedule("16:00", "GBLA")  # Jadwal berubah -> observer dapat notifikasi


if __name__ == "__main__":  # Biar main() kepanggil saat run demo.py
    main()  # Jalankan demo
