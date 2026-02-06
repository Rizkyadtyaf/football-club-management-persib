from typing import Iterator, Iterable, Optional
from player import Player


class SquadIterator:  # Iterator default untuk list pemain
    def __init__(self, players: Iterable[Player]) -> None:
        self._players = list(players)
        self._index = 0

    def __iter__(self) -> "SquadIterator":
        return self

    def __next__(self) -> Player:
        if self._index >= len(self._players):
            raise StopIteration
        player = self._players[self._index]
        self._index += 1
        return player


class RoleFilterIterator:  # Iterator untuk filter berdasarkan role (DEF/MID/ATT/GK)
    def __init__(self, players: Iterable[Player], role: str) -> None:
        self._players = list(players)
        self._role = role.upper()
        self._index = 0

    def __iter__(self) -> "RoleFilterIterator":
        return self

    def __next__(self) -> Player:
        while self._index < len(self._players):
            player = self._players[self._index]
            self._index += 1
            if player.role == self._role:
                return player
        raise StopIteration


class PositionFilterIterator:  # Iterator untuk filter posisi spesifik (mis: GK, CB, CM, ST)
    def __init__(self, players: Iterable[Player], position: str) -> None:
        self._players = list(players)
        self._position = position.upper()
        self._index = 0

    def __iter__(self) -> "PositionFilterIterator":
        return self

    def __next__(self) -> Player:
        while self._index < len(self._players):
            player = self._players[self._index]
            self._index += 1
            if player.position == self._position:
                return player
        raise StopIteration
