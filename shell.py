from core import *


def print_stats(player_1, player_2):
    print(player_1)
    print(player_2)


def print_classes():
    print('[1] Warrior: blah blah blah')


def make_gladiator():
    name = input('What is your name? ').upper()
    print_classes()
    response = input('Pick your class >>> ').strip()
    print()
    if response == '1':
        return Warrior(str(name), 100, 20, 0, 10, 20)
    else:
        print('Invalid class number.')


def print_moves():
    print("[1] Attack\n[2] Heal\n[3] Skip\n[4] Quit\n[5] Special\n")


def battle(player, other_player):
    while True:
        print_moves()
        response = input('What would you like to do {}? '.format(player.name))
        if response == '1':
            return player.attack(other_player)
        elif response == '2':
            return player.heal()
        elif response == '3':
            player.power += 25
            return None
        elif response == '4':
            exit()
        elif response == '5':
            return player.special(other_player)
        else:
            ('Not a valid number')


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
