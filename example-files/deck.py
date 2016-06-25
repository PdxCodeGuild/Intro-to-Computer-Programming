#!/usr/bin/env python

# standard python library
from collections import namedtuple
from random      import shuffle
from itertools   import cycle

# pip installed packages
from names       import get_full_name

"""
The goal of this assignment is to have you define your own game rules

Start with BlackJack and move onto another game like go fish
"""

def new_deck():
    # I have made a deck for you!
    Card = namedtuple('Card', ['suit', 'face'])

    deck = []
    for suit in ['H', 'C', 'S', 'D']:
        for face in ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']:
             deck.append(Card(suit=suit, face=face))
    shuffle(deck)
    return deck

...

def main():
    deck          = new_deck()
    count_players = 3
    players       = dict()

    for _ in range(count):
        hand_for_player = []
        name_for_player = get_full_name()
        players[name_for_player] = hand_for_player
        ...

    for index, name in enumerate(cycle(players.keys())):
        print('{} : takes turn {}'.format(name, index))
        ...
        hand_for_player = players[name]
        print('    {}'.format(hand_for_player))
        task = input('what would you like to do? ')
        ...

        print(' \n\n --- ')

    ...


if __name__ == '__main__':
    main()
