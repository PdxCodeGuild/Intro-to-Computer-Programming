#!/usr/bin/env python3

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
    Card = namedtuple('Card', ['suit', 'face'])

    deck = []
    for suit in ['H', 'C', 'S', 'D']: # Hearts, Clubs, Spades, Diamonds
        for face in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']: # A=1; J, Q, K = 10
             deck.append(Card(suit=suit, face=face))
    shuffle(deck)
    return deck

...

def deal_cards(players, deck):
    for player_name in players:
        # player gets a card 
        players[player_name].append(pop_deck(deck))
        players[player_name].append(pop_deck(deck))
        # players[player_name].append(deck.pop())
        # print player cards
        print_player_cards(player_name, players)
        
# ----------------------
# pop the card from the deck 
def pop_deck(deck): 
    return deck.pop()

# ----------------------
# print the deck of card
def print_deck(deck): 
    # print(deck) 
    print('deck of cards are: ')
    for n, card_name in enumerate(deck, 1):
        print(' card = {}: {} '.format(n, card_name))


def print_collection(collection):
    print('contents of collection are: ')
    for n, value in enumerate(collection, 1):
        print(' card = {}: {} '.format(n, value))

# ----------------------
# print the player names 
def print_player_names(players):
    #print(players)
    print('players are: ') 
    for n, player_name in enumerate(players, 1):
        print('{}: {} '.format(n, player_name))


# ----------------------
# print player cards 
def print_player_cards(player_name, players): 
    print('player name =  {}'.format(player_name)) 
    print('cards = {}'.format(players.get(player_name)))


def main():
    deck    = new_deck()
    print_deck(deck)
    count   = 3
    players = dict() # dict with key = players name, value = card  

    for _ in range(count):
        player_name = get_full_name()
        players[player_name] = []

    print_player_names(players) 

    deal_cards(players, deck) # give two card to each player


    for index, name in enumerate(cycle(players.keys())):
        print('{} : takes turn {}'.format(name, index))
        print('    {}'.format(players[name]))
        task = input('what would you like to do? ')
        ...

        print(' \n\n --- ')

    ...


if __name__ == '__main__':
    main()
