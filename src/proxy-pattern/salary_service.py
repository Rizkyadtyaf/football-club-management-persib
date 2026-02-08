class RealSalaryService:
    def __init__(self):
        self._db = {
            "Player A": 250_000_000,
            "Player B": 175_000_000,
        }

    def get_salary(self, player_name: str) -> int:
        return self._db.get(player_name, 0)
