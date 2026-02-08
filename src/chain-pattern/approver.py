from __future__ import annotations
from typing import Optional
from request import TransferRequest


class Approver:
    def __init__(self, next_approver: Optional["Approver"] = None):
        self.next = next_approver

    def approve(self, req: TransferRequest) -> bool:
        if self._can_approve(req):
            print(f"[APPROVED] {self.__class__.__name__}: {req.player_name}")
            return True

        if self.next:
            print(f"[PASS] {self.__class__.__name__} -> {self.next.__class__.__name__}")
            return self.next.approve(req)

        print(f"[REJECTED] End of chain: {req.player_name}")
        return False

    def _can_approve(self, req: TransferRequest) -> bool:
        raise NotImplementedError


class Scout(Approver):
    def _can_approve(self, req: TransferRequest) -> bool:
        return req.fee_miliar <= 2


class HeadCoach(Approver):
    def _can_approve(self, req: TransferRequest) -> bool:
        return req.weekly_wage_juta <= 150


class TechnicalDirector(Approver):
    def _can_approve(self, req: TransferRequest) -> bool:
        return req.fee_miliar <= 10


class FinanceDirector(Approver):
    def _can_approve(self, req: TransferRequest) -> bool:
        annual_wage_juta = req.weekly_wage_juta * 52
        total_cost_juta = req.fee_miliar * 1000 + annual_wage_juta
        return total_cost_juta <= 20000


class CEO(Approver):
    def _can_approve(self, req: TransferRequest) -> bool:
        return True
