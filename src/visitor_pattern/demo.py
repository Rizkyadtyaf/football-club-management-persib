from visitor import Visitor
from player import Player

class SalaryVisitor(Visitor):
    def visit_player(self, player):
        bonus = player.goals * 1_000_000
        print(f"{player.name} mendapat bonus: Rp {bonus:,}")

print("===== DEMO VISITOR PATTERN PERSIB =====")

player1 = Player("Beckham Putra", 2)
player2 = Player("David da Silva", 3)

visitor = SalaryVisitor()

player1.accept(visitor)
player2.accept(visitor)
