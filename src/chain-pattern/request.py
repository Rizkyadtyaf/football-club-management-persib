from dataclasses import dataclass

@dataclass
class TransferRequest:
    player_name: str
    fee_miliar: float
    weekly_wage_juta: float
