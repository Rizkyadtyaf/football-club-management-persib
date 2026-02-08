from player import Player


class PlayerDecorator(Player):
    def __init__(self, wrapped: Player):
        self._wrapped = wrapped
        super().__init__(wrapped.name, wrapped.position)

    def profile(self) -> str:
        return self._wrapped.profile()

    def availability(self) -> str:
        return self._wrapped.availability()


class Captain(PlayerDecorator):
    def profile(self) -> str:
        return self._wrapped.profile() + " [CAPTAIN]"


class Injured(PlayerDecorator):
    def availability(self) -> str:
        return "Unavailable (Injured)"


class OnLoan(PlayerDecorator):
    def profile(self) -> str:
        return self._wrapped.profile() + " [ON LOAN]"
