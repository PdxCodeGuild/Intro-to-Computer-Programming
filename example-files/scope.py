#!/usr/bin/env python3

def one(word):
    print('Jenny {} to the street.'.format(word))


def two(word):
    print('We used the {} to fassen the two pieces of wood together.'.format(word))


def three(word):
    print('He was struck by a {} of lightning'.format(word))


def context():
    item = 'bolt'

    one(word=item)
    _ = input('what does "{}" mean in this context?'.format(item))

    two(word=item)
    _ = input('what does "{}" mean in this context?'.format(item))

    three(word=item)
    _ = input('what does "{}" mean in this context?'.format(item))


context()

