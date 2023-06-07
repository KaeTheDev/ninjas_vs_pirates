class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def swordAttack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def tossBottle(self, ninja):
        ninja.health -= self.strength
        return self
    
    def drinkWhiskey(self, health):
        self.health += 10
        return self