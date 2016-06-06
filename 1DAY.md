# Day 1 - Setup Environment, Shell, Basic Programming, First Exercise
## Setup Environment
1. [Atom](https://github.com/selassid/codeguild/blob/master/notes/atom.md) and [Tricks](https://github.com/selassid/codeguild/blob/master/notes/atom-python.md)
2. [Python](https://github.com/selassid/codeguild/blob/master/notes/py.md)

## Shell
A shell is another way for you to interact with your computer. This is often a CLI (Command Line Interface) as apposed to a GUI (Graphical User Interface). Developers often favor CLI due to the ease of automating repetative tasks. We will to look at [Powershell/Bash](https://github.com/selassid/codeguild/blob/master/notes/cli.md) and how it compares to your GUI.

[Learn Python the Hard Way - Apendix A](http://learnpythonthehardway.org/book/appendixa.html)

## Python
In this course we are introducing you to python. Our first exercise will show you how to make a python file, establish a workflow, understand variables and introduce some programming vocabulary.

I suggest having `ipython shell` and your `atom editor` both open in your workspace, until you develop your own work flow. Those with mac or linux can install use `bpython shell` if they prefer.

### disabling magic in your ipython environment
```
$ ipython3
Python 3.4.2 (default, Jul  9 2015, 17:24:30)
Type "copyright", "credits" or "license" for more information.

IPython 4.1.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: ip = get_ipython()

In [2]: ip.Completer.matchers.remove(ip.Completer.magic_matches)

In [3]:
```

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

# pattern matched assignment
b, a = 'neat!', 'thats'
print(a, b)

# What do you think this does?
x, y = y, x
print(x, y)
```

### print()
1. The `print()` function allows us to write content to the `console`, also called a `terminal` or `CLI`.
2. You may find **reputable** resources online that just don't work. Most people's first experience with this is in python's print. Programming languages have release `versions` that may have different, often competing, `syntax`. This, [Python 2.7 vs Python 3.x](https://www.webucator.com/blog/2016/03/still-using-python-2-it-is-time-to-upgrade/), article can help you drink the Python 3.x Kool Aid.
```python
#!/usr/bin/env python3

print("THIS IS HOW YOU PRINT IN PYTHON 3.x")
```
```python
#!/usr/bin/env python2.7

print "THIS IS HOW YOU PRINT IN PYTHON 2.x"
```
### String concatenation and format() method
```python
#!/usr/bin/env/python

def pause():
    # pause program until user input
    _ = input()


x = 'elephant'
y = 'pig'

# string concatination
print(x, y)
print(x + y)
print(x*3 + y*2)

z = x + y
print(z)

z = x + ' loves ' + y
print(z)

# use of .format method
z = '{} loves {}!'
print(z.format(x, y))
print(z.format(y, x))
print(z.format('philip', 'hats'))

```

```
#!/usr/bin/env python
# what is a panagram?
story_tamplate = 'The exodus of {adjective_one} {noun_one}s is craved by {adjective_one} {noun_two}s.'
print(story_template.format(adjective_one='jazzy', noun_one='pidgeon', adjective_two='squeamish', noun_two='walker'))
print(story_template.format(adjective_one='funky', noun_one='wizard', adjective_two='spanish', noun_two='camel'))

# can we split this up?
s = story_template.format(
    adjective_one='lusting',
    noun_one='lion',
    adjective_two='lackadaisical',
    noun_two='lemur',
    )
print(s)

# can we check if something is a panagram?
print('a', str.count(s, 'a'))
print('b', str.count(s, 'b'))
print('c', str.count(s, 'c'))
print('d', str.count(s, 'd'))
print('e', str.count(s, 'e'))
print('f', str.count(s, 'f'))
print('g', str.count(s, 'g'))

print('h', s.count('h'))
print('i', s.count('i'))
print('j', s.count('j'))
print('k', s.count('k'))
print('l', s.count('l'))
print('m', s.count('m'))

...

print('x', s.count('x'))
print('y', s.count('y'))
print('z', s.count('z'))
```

### Input()
```python
#!/usr/bin/env python

x = input("Into variable 'x' i will save the value :")
print("into x I saved the value {x}".format(x=x))

x = input('again :')
print("into x I saved the value {x}".format(x=x))

y = input('what about something else?')
print(y, 'has been saved into a variable in my program.')

print('again :')
y = input()
print(y, 'has been saved into a variable in my program.')
```

### Have the students make a [Madlib](./example-files/madlib.py)

