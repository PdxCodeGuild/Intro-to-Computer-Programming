# Finding Modules

![Names search](./example-files/search.png)

![Names search](./example-files/find.png)

```
$ pip install --user names
```

# Blackjack template

```python
#!/usr/bin/env python                                                                                    

from collections import namedtuple
from random      import shuffle
from itertools   import cycle
from names       import get_full_name

"""                                                                                                      
The goal of this assignment is to have you define your own game rules                                    
"""

def new_deck():
    Card = namedtuple('Card', ['suit', 'face'])

    deck = []
    for suit in ['H', 'C', 'S', 'D']:
        for face in ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']:
             deck.append(Card(suit=suit, face=face))
    shuffle(deck)
    return deck


...


def main():
    deck    = new_deck()
    count   = 3
    players = dict((get_full_name(), []) for _ in range(count))

    for index, name in enumerate(cycle(players.keys())):
        print('{} : takes turn {}'.format(name, index))
        print('    {}'.format(players[name]))
        task = input('what would you like to do? ')
        ...

        print(' \n\n --- ')


if __name__ == '__main__':
    main()
```
