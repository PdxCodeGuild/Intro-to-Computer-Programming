# Day 3
### Functions
```python
#!/usr/bin/env python

def first_example():
    pass

def second_example():
    return 5

def third_example(x):
    return x
```
```python
#!/usr/bin/env python

x = 7

def fourth_example(x):
    return x + x

print(fourth_example(3))
```
```python
#!/usr/bin/env python

def plus(x, func):
    return x + func(x)

def square(x):
    return x ** 2

print(plus(5, square))
```
```python

#!/usr/bin/env python
def func(x):
    return x * x

li = [3, 4, 5, 6, 7, 8, 9, 10]

_ = input()
for element in li:
    print(element)

_ = input()
for index, value in enumerate(li):
    li[index] = func(value)

print(li)
```

```python
#!/usr/bin/env python

"""
'scope of a variable is defined at the level of assignment' -- Elana Hashman
https://www.youtube.com/watch?v=CjYEpVNbM-s
"""

cat = 'meow'

def cat_changer():
    cat = 'purr'
    print('inside cat: ', cat)

_ = input()
cat_changer()
print('outside cat: ', cat)

_ = input()

def fifth_example(x, y):
    return x + y

def sixth_example(x):
    def fifth_example(x, y):
        return x * y

    return fifth_example(x, x)

_ = input()
print(fifth_example(10))

_ = input()
print(sixth_example(10))
```

### List Comprehensions

## Hangman
Implement hangman from this template. The `...` are used to denote where code will need to be added.

```python
def set_word():
    word = input('What phrase would you like to hang? ')
    template = ['_'] * len(word)

    space    = ' '
    indicies = get_index(space, word)
    template = update(space, indicies, template)

    return word, template


def get_index(char, word):
    # return list of index values of character in word
    ...


def update(char, indicies, template):
    # update the indicies of template with char, then return template
    ...


def iscomplete(word, template):
    # do the word and template represent the same content?
    ...


def get_character():
    # get a character from the command line as user input
    ...


def take_turn(word, template):
    ch = get_character()
    indicies = get_index(ch, word)
    template = update(ch, indicies, template)
    print(template)


def main():
    win   = False
    word, template = set_word()

    for turn in range(10):
        if iscomplete(word, template):
            ...

        take_turn(word, template)

    if win:
        ...
    else:
        ...


if __name__ == '__main__':
    main()

```

 - Review dictionary methods
 - [Phone book challenge](./example-files/phonebook.py) – Have students make a phonebook program that will give the user a menu and have the capability to search, add, change and remove entries.
