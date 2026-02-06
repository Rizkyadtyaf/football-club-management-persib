from dataclasses import dataclass  # Biar event rapi
from datetime import datetime  # Timestamp event


@dataclass(frozen=True)
class BaseEvent:  # Kelas dasar semua event
    occurred_at: datetime  # Waktu event terjadi


@dataclass(frozen=True)
class PlayerStatusChangedEvent(BaseEvent):  # Event perubahan status pemain
    player_name: str
    old_status: str
    new_status: str


@dataclass(frozen=True)
class TrainingScheduleChangedEvent(BaseEvent):  # Event perubahan jadwal latihan
    date: str
    old_time: str
    new_time: str
    location: str
