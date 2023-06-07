print(f'The warrior: {warrior.name} approaches the wizard: {wizard.name}!')

while warrior.hp > 0 and wizard.hp > 0:
    player_input = ""
    while not player_input == "1" and not player_input == "2":
        # Using the input method, we can request something from the user in the terminal.
        player_input = input("What to do?\n 1) Attack\n 2) Use skill\n <=========>")
        if player_input == "1":
            warrior.attack(wizard)
        elif player_input == "2":
            warrior.Warrior_Rage(wizard)
        else:
            print("Choose a valid option! (1 or 2)")
        
    coin_toss = random.randint(1,2)
    if coin_toss == 1:
        wizard.attack(warrior)
    else:
        wizard.magearmor()

    rounds++
    if warrior.hp > 0:
        print("You win!")
    elif wizard.hp <= 0:
        print("Draw!")
    else:
        print("The Wizard Wins!")