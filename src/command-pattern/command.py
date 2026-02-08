from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TrainCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.train()


class TacticalCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.tactical_session()


class RestCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.rest()


class MacroCommand(Command):
    """Menjalankan banyak command sekaligus"""
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()
