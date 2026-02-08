from player import Player
from coach import Coach
from command import TrainCommand, TacticalCommand, RestCommand, MacroCommand


def main():
    print("===== COMMAND PATTERN =====")

    player = Player("Beckham Putra")
    coach = Coach("Bojan Hodak")

    training_program = MacroCommand()
    training_program.add_command(TrainCommand(player))
    training_program.add_command(TacticalCommand(player))
    training_program.add_command(RestCommand(player))

    coach.give_instruction(training_program)


if __name__ == "__main__":
    main()
