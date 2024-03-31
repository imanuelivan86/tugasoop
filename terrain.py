from unit import Unit

class Terrain(Unit):
    def __init__(self, name, movement_cost):
        super().__init__(name, health=0, attack_damage=0)  
        self.movement_cost = movement_cost

    def display_info(self):
        super().display_info()
        print(f"Movement Cost: {self.movement_cost}")
