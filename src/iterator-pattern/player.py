from dataclasses import dataclass  # Biar class Player ringkas (data container)

@dataclass(frozen=True)
class Player:
    number: int      # Nomor punggung
    name: str        # Nama pemain
    position: str    # Posisi ringkas (GK/DF/MF/FW)
    role: str        # Role umum (GK/DEF/MID/ATT)
