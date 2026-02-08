class Coach:
    def __init__(self, name):
        self.name = name

    def give_instruction(self, command):
        print(f"Pelatih {self.name} memberikan instruksi:")
        command.execute()
