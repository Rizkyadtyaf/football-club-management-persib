from user import User
from salary_service import RealSalaryService


class SalaryServiceProxy:
    def __init__(self, real: RealSalaryService, user: User):
        self._real = real
        self._user = user

    def get_salary(self, player_name: str):
        if self._user.role not in ("finance", "ceo"):
            print(f"Access denied for role '{self._user.role}'")
            return None
        return self._real.get_salary(player_name)
