class Unit:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def display_info(self):
        print(f"Unit: {self.name}, Health: {self.health}, Attack Damage: {self.attack_damage}")
