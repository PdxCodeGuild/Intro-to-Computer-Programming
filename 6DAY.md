# Review of Scoping Problems

```python
#!/usr/bin/env python3

def one(word):
    print('Jenny {} to the street.'.format(word))


def two(word):
    print('We used the {} to fassen the two pieces of wood together.'.format(word))


def three(word):
    print('He was struck by a {} of lightning'.format(word))


def context():
    item = 'bolt'

    one(item)
    _ = input('what does "{}" mean in this context?'.format(item))

    two(item)
    _ = input('what does "{}" mean in this context?'.format(item))

    three(item)
    _ = input('what does "{}" mean in this context?'.format(item))

```

# Walk Through Solutions of BlackJack

# Assignment
For this assignment, you will get to choose your own task. If you cannot think of one, select from the list below.
* Image Manipulation (ie. Rotate, Extract RGB, Shrink)
* Save image of plotted Graph (ie. Histogram, Equation, Pie-Chart) [May be harder on Windows]
* System Administration (ie. Launch Command, Access Environment Variables)
