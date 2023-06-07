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
        jack_sparrow.show_stats()
    elif player_input == "2":
        jack_sparrow.drinkWhiskey()
        jack_sparrow.show_stats()
    else:
        print("Choose a valid option! (1 or 2)")
    coin_toss = random.randint(1,2)
    if coin_toss == 1:
        jack_sparrow.tossBottle(sensei)
    else:
        sensei.meditate()

print("Game Over")

print("\n==================\n")



print("\n==================\n")

print("ROUND ONE")

# USE THE SPEED TO DECIDE WHO GOES FIRST
# michelangelo.attack(jack_sparrow)
jack_sparrow.drinkWhiskey()



rounds += 1
if jack_sparrow.health > 0:
    print("You win!")
elif jack_sparrow.health <= 0:
    print("Draw!")
else:
    print("The Pirate Wins!")