import random

from classes.ninja import Ninja
from classes.pirate import Pirate

# create players
sensei = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

rounds = 0

while sensei.health > 0 and jack_sparrow.health > 0:
    player_input = ""
    while not player_input == "1" and not player_input == "2":
        # Using the input method, we can request something from the user in the terminal.
        player_input = input("What to do?\n 1) Attack\n 2) Use skill\n <=========> ")
    if player_input == "1":
        sensei.punchAttack(jack_sparrow)
    elif player_input == "2":
        jack_sparrow.drinkWhiskey(Pirate)


print("Both players intial stats: ")

print("\n==================\n")

jack_sparrow.show_stats()
sensei.show_stats()

print("\n==================\n")

print("ROUND ONE")

# USE THE SPEED TO DECIDE WHO GOES FIRST
# michelangelo.attack(jack_sparrow)
jack_sparrow.drinkWhiskey("Crown Royal")
