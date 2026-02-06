from observer import Observer  # Interface observer
from events import BaseEvent, PlayerStatusChangedEvent, TrainingScheduleChangedEvent  # Event-event


class CoachNotifier(Observer):  # Observer untuk pelatih
    def update(self, event: BaseEvent) -> None:
        if isinstance(event, PlayerStatusChangedEvent):
            print(f"[PELATIH] {event.player_name}: {event.old_status} -> {event.new_status}")
        elif isinstance(event, TrainingScheduleChangedEvent):
            print(f"[PELATIH] Jadwal {event.date} pindah ke {event.new_time} di {event.location}")


class ManagerNotifier(Observer):  # Observer untuk manajer
    def update(self, event: BaseEvent) -> None:
        if isinstance(event, PlayerStatusChangedEvent):
            print(f"[MANAJER] Status pemain {event.player_name}: {event.new_status}")


class MedicalStaffNotifier(Observer):  # Observer untuk tim medis
    def update(self, event: BaseEvent) -> None:
        if isinstance(event, PlayerStatusChangedEvent) and event.new_status == "INJURED":
            print(f"[MEDIS] Perlu pemeriksaan untuk {event.player_name}")