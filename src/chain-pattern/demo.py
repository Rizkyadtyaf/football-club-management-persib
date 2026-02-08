from request import TransferRequest
from approver import Scout, HeadCoach, TechnicalDirector, FinanceDirector, CEO

if __name__ == "__main__":
    chain = Scout(
        HeadCoach(
            TechnicalDirector(
                FinanceDirector(
                    CEO(None)
                )
            )
        )
    )

    req1 = TransferRequest("Striker Target", fee_miliar=1.5, weekly_wage_juta=80)
    req2 = TransferRequest("Bintang Liga", fee_miliar=8, weekly_wage_juta=220)

    print("=== Request 1 ===")
    chain.approve(req1)
    print("\n=== Request 2 ===")
    chain.approve(req2)
