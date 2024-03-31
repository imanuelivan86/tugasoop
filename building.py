from unit import Unit

class Building(Unit):
    def __init__(self, name, health, attack_damage, build_time):
        super().__init__(name, health, attack_damage)
        self.build_time = build_time

    def display_info(self):
        super().display_info()
        print(f"Build Time: {self.build_time} seconds")
