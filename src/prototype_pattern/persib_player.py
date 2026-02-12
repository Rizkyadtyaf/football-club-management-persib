from prototype_interface import PlayerPrototype
import copy

class PersibPlayer(PlayerPrototype):
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Nama      : {self.name}")
        print(f"Posisi    : {self.position}")
        print(f"Gaji      : Rp {self.base_salary:,}")
