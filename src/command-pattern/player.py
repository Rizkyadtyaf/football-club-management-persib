class Player:
    def __init__(self, name):
        self.name = name

    def train(self):
        print(f"{self.name} menjalani latihan fisik")

    def tactical_session(self):
        print(f"{self.name} mengikuti latihan taktik")

    def rest(self):
        print(f"{self.name} menjalani pemulihan")
