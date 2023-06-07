class Ninja:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n"
        )

    def punchAttack(self, pirate):
        pirate.health -= self.strength
        return self

    def highKick(self, pirate):
        pirate.health -= self.strength
        return self

    def meditate(self):
        self.health += 15
        return self
