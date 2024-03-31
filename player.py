class Player:
    def __init__(self, name):
        self.name = name
        self.resources = 1000  # atribut untuk sumber daya pemain

    def display_resources(self):
        print(f"{self.name}'s resources: {self.resources}")
