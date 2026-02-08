class Player:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def profile(self) -> str:
        return f"{self.name} ({self.position})"

    def availability(self) -> str:
        return "Available"
