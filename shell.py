from core import *


def print_stats(player_1, player_2):
    print()
    print(player_1)
    print(player_2)
    print()


def print_classes():
    print('--CHARACTERS--')
    print('[1] Warrior\n[2] Healer')


def print_move_info():
    print("\n--Basic Attacks--")
    print(
        'Attack: Does damage to opponent and adds 15 Rage/Power\nHeal: Adds 10 Health at the cost of 10 Power.\nPass: Skipps your turn but gives you 25 Power.\nQuit: You exit the game.\n'
    )
    print('--Special Abilities--')
    print("Slash: Does 50 damage to opponent at the cost of 45 power.")
    print("Healing: Add 50 Health to the user at the cost of 45 power.")
    print()


def make_gladiator():
    name = input('What is your name? ').upper()
    print_classes()
    response = input('Pick your class >>> ').strip()
    print()
    if response == '1':
        return Warrior(str(name), 100, 20, 0, 10, 20, "Slash")
    if response == '2':
        return Healer(str(name), 100, 0, 15, 8, 16, "Healing")
    else:
        print('Invalid class number.')


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


def main():
    player_1 = make_gladiator()
    player_2 = make_gladiator()
    print_stats(player_1, player_2)
    winner(player_1, player_2)


if __name__ == '__main__':
    main()
