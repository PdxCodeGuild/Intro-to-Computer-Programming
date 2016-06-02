# Day 1 - Setup Environment, Shell, Basic Programming, First Exercise
## Setup Environment
1. [Atom](https://github.com/selassid/codeguild/blob/master/notes/atom.md) and [Tricks](https://github.com/selassid/codeguild/blob/master/notes/atom-python.md)
2. [Python](https://github.com/selassid/codeguild/blob/master/notes/py.md)

## Shell
A shell is another way for you to interact with your computer. This is often a CLI (Command Line Interface) as apposed to a GUI (Graphical User Interface). Developers often favor CLI due to the ease of automating repetative tasks. We will to look at [Powershell/Bash](https://github.com/selassid/codeguild/blob/master/notes/cli.md) and how it compares to your GUI.

## Python
In this course we are introducing you to python. Our first exercise will show you how to make a python file, establish a workflow, understand variables and introduce some programming vocabulary.

### Variables and Using Strings
```python
#!/usr/bin/env python

# assignment
x = 'cat'
print(x)

# reasignment
x = 'dog'
print(x)

x = 'cat'
x = 'dog'
print(x)

# multiple variables
y = 'cat'
print(x, y)

# What do you think this does?
x, y = y, x
print(x, y)
```

### print()
1. The `print()` function allows us to write content to the `console`, also called a `terminal` or `CLI`.
2. You may find resources, from reputable resources, online that don't work. Most people's first expirience with this is in python's print. Programming languages have release `versions` that may have different, often competing, `syntax`. This, [Python 2.7 vs Python 3.x](https://www.webucator.com/blog/2016/03/still-using-python-2-it-is-time-to-upgrade/), article can help you drink the Python 3.x Kool Aid.

### String concatenation
### String method .format()
### Input()
### Have the students make a [Madlib](./example-files/madlib.py)

