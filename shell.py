from core import *


def print_stats(player_1, player_2):
    print()
    print(player_1)
    print(player_2)
    print()


def print_classes():
    print('--CHARACTERS--')
    print('[1] Warrior\n[2] Healer\n[3] Angel\n[4] King\n')


def print_move_info():
    print("\n--Basic Attacks--")
    print(
        'Attack: Does damage to opponent and adds 15 Rage/Power\nHeal: Adds 10 Health at the cost of 10 Power.\nPass: Skipps your turn but gives you 25 Power.\nQuit: You exit the game.\n'
    )
    print('--Special Abilities--')
    print("Slash: Does 50 damage to opponent at the cost of 45 power.")
    print("Healing: Add 50 Health to the user at the cost of 45 power.")
    print(
        "Sin Cleansing: Removes the Rage from your opponent and damages them slightly"
    )
    print()


def pick_class(name: str) -> Gladiator:
    while True:
        print_classes()
        response = input('Pick your class >>> ').strip()
        print()
        if response == '1':
            return Warrior(str(name), 100, 20, 0, 10, 20, "Slash")
        elif response == '2':
            return Healer(str(name), 110, 0, 15, 8, 16, "Healing")
        elif response == '3':
            return Angel(str(name), 100, 0, 15, 8, 18, "Sin Cleansing")
        elif response == '4':
            return King(str(name), 100, 15, 100, 6, 15, "Royal Power")

        else:
            print('Invalid class number.')


def name_gladiator():
    while True:
        name = input('What is your name? ').upper()
        if name.strip() == '':
            print('\n Please enter a valid name.\n')
        else:
            return name


def make_gladiator():
    name = name_gladiator()
    return pick_class(name)


def print_moves():
    print("[1] Attack\n[2] Heal\n[3] Skip\n[4] Quit\n[5] Special\n")
    print("Type 'help' to get each information about each move")


def battle(player, other_player):
    while True:
        print_moves()
        response = input('What would you like to do {}? '.format(
            player.name)).strip().lower()
        if response == '1':
            print("{} just attacked.".format(player.name))
            return player.attack(other_player)
        elif response == '2':
            if player.power >= 10:
                print("{} just healed".format(player.name))
                return player.heal()
            else:
                print("Not enough Power")
        elif response == '3':
            player.power += 25
            print("{} has skipped.".format(player.name))
            return None
        elif response == '4':
            print("{} just Quit the match making them the loser.".format(
                player.name))
            exit()
        elif response == '5':
            if player.special_is_possible() == True:
                print("{} used {}".format(player.name, player.ability))
                return player.special(other_player)
            else:
                print('Not enough power!')
        elif response == 'help':
            print_move_info()
        else:
            print('Not a valid number')


def bot_battle(player, other_player):
    while True:
        print_moves()
        response = choice([1, 1, 1, 2, 2, 3, 5])
        if response == 1:
            print("{} just attacked.".format(player.name))
            return player.attack(other_player)
        elif response == 2:
            if player.power >= 10:
                print("{} just healed".format(player.name))
                return player.heal()
            else:
                print("Not enough Power")
        elif response == 3:
            player.power += 25
            print("{} has skipped.".format(player.name))
            return None
        elif response == 5:
            if player.special_is_possible() == True:
                print("{} used {}".format(player.name, player.ability))
                return player.special(other_player)
            else:
                print('Not enough power!')
        elif response == 'help':
            print_move_info()
        else:
            print('Not a valid number')


def winner(player, other_player):
    while True:
        if player.is_dead() == False and other_player.is_dead() == False:
            battle(player, other_player)
            print_stats(player, other_player)
            if other_player.is_dead() == True:
                print("{} Wins!".format(player.name))
                break
            elif player.is_dead() == True:
                print("{} Wins!".format(other_player.name))
                break
            battle(other_player, player)
            print_stats(player, other_player)
            if player.is_dead() == True:
                print("{} Wins!".format(other_player.name))
                break
            elif other_player.is_dead() == True:
                print("{} Wins!".format(player.name))
                break


def winner_against_bots(player, names):
    shuffle(names)
    name = player_bot_name(names)
    other_player = make_bot(name)
    print_stats(player, other_player)
    while True:
        if player.is_dead() == False and other_player.is_dead() == False:
            battle(player, other_player)
            print_stats(player, other_player)
            if other_player.is_dead() == True:
                print("{} Wins!".format(player.name))
                return next_round(player, names)
            elif player.is_dead() == True:
                print("{} Wins!".format(other_player.name))
                break
            bot_battle(other_player, player)
            print_stats(player, other_player)
            if player.is_dead() == True:
                print("{} Wins!".format(other_player.name))
                break
            elif other_player.is_dead() == True:
                print("{} Wins!".format(player.name))
                return next_round(player, names)


def player_bot_name(names):
    name = names.pop()
    return name


def player_bot_class(name: str) -> Gladiator:
    while True:
        response = randint(1, 4)
        if response == 1:
            return Warrior(str(name), 100, 20, 0, 10, 20, "Slash")
        elif response == 2:
            return Healer(str(name), 110, 0, 15, 8, 16, "Healing")
        elif response == 3:
            return Angel(str(name), 100, 0, 15, 8, 18, "Sin Cleansing")
        elif response == 4:
            return King(str(name), 100, 15, 100, 6, 15, "Royal Power")


def make_bot(name):
    return player_bot_class(name)


def next_round(player, names):
    if len(names) > 0:
        print('You advance to the next boss')
        print('^\n^^\n^^^\n')
        return winner_against_bots(player, names)
    else:
        print('You\'ve beaten all the bosses!')


def single_or_multiplayer():
    response = input(
        'Is this a [S]ingle or [M]ultiplayer Game? >>> ').upper().strip()
    if response == 'M':
        player_1 = make_gladiator()
        player_2 = make_gladiator()
        print_stats(player_1, player_2)
        winner(player_1, player_2)
    elif response == 'S':
        names = ["Captain Crunch", "Small Child", "Silly Killy"]
        player_1 = make_gladiator()
        winner_against_bots(player_1, names)


def main():
    single_or_multiplayer()


if __name__ == '__main__':
    main()
