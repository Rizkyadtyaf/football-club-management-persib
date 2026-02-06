# PersibSquad acts as Aggregate in Iterator Pattern

from typing import List, Iterator
from player import Player
from iterators import SquadIterator, RoleFilterIterator, PositionFilterIterator


class PersibSquad:  # Aggregate/Collection: menyimpan daftar pemain Persib
    def __init__(self) -> None:
        self._players: List[Player] = []  # Penyimpanan internal

    def add_player(self, player: Player) -> None:  # Tambah pemain ke skuad
        self._players.append(player)

    def __iter__(self) -> Iterator[Player]:  # Iterator default (semua pemain)
        return SquadIterator(self._players)

    def iter_by_role(self, role: str) -> Iterator[Player]:  # Iterator filter by role
        return RoleFilterIterator(self._players, role)

    def iter_by_position(self, position: str) -> Iterator[Player]:  # Iterator filter posisi
        return PositionFilterIterator(self._players, position)
