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

def create_deck():
    Card = namedtuple('Card', ['suit', 'face'])

    deck = []
    for suit in ['H', 'C', 'S', 'D']:
        for face in ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']:
             deck.append(Card(suit=suit, face=face))
    shuffle(deck)
    return deck

...

def ask_player():
    turn_choice = input('would you like to stand or draw card:' )
    return turn_choice

def stand(hand):
    current_score = add_score(hand)
    return current_score

def draw_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    return hand

def add_score(hand):
    score = 0
    for index, card in enumerate(hand):
        x = card.face
        if x in ['J', 'Q', 'K']:
            x = 10
        elif x == 'A':
            x = 1
        else:
            x = int(card.face) # turns '4' into 4

        score = x + score
    return score


def compare_to(score, maximumvalue=21):
    return maximumvalue - score


def main():
    deck    = create_deck()
    number_of_players   = 3
    players = dict()
    tops = 15

    for _ in range(number_of_players):
        name = get_full_name()
        players[name] = []
        draw_card(deck, players[name])
        draw_card(deck, players[name])

    for index, name in enumerate(cycle(players.keys())):
        print('{} : takes turn {}'.format(name, index))
        print('    {}'.format(players[name]))
        turn_choice = ask_player()

        hand = players.get(name)

        if turn_choice == 'stand':
            players_score = stand(hand)
        else:
            draw_card(deck, hand)
            players_score = add_score(hand)
            if compare_to(players_score, tops) < 0:
                print('Bust!')
                players.pop(name)
                break

    final_scores = []
    for player_name in players:
        players_score = add_score(players.get(player_name))
        print(players_score, player_name)
        compared_score = compare_to(players_score, tops)
        store_value = compared_score, player_name
        final_scores.append(store_value)

    winner = min(final_scores)
    print(winner)
    print(' \n\n --- ')




if __name__ == '__main__':
    main()
