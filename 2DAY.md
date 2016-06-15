# Day 2 - Introduction to Types and Control Flow
## [Primitive types](https://docs.python.org/3.5/library/stdtypes.html) and Exploration of Types
In this section we develop a more complete understanding of types. In your career you will likely run into code that is confusing. Here we gain the skills needed to better explore types.

### [String](https://docs.python.org/3.5/library/string.html)
```
$ ipython3 -i unmagic.py
Python 3.4.2 (default, Jul  9 2015, 17:24:30) 
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: type('c')
Out[1]: str

In [2]: "cat"
Out[2]: 'cat'

In [3]: type('cat')
Out[3]: str

In [4]: 'cat' + 'dog'
Out[4]: 'catdog'

In [5]: type('cat' + 'dog')
Out[5]: str

In [6]: str.
str.capitalize    str.isidentifier  str.rindex
str.casefold      str.islower       str.rjust
str.center        str.isnumeric     str.rpartition
str.count         str.isprintable   str.rsplit
str.encode        str.isspace       str.rstrip
str.endswith      str.istitle       str.split
str.expandtabs    str.isupper       str.splitlines
str.find          str.join          str.startswith
str.format        str.ljust         str.strip
str.format_map    str.lower         str.swapcase
str.index         str.lstrip        str.title
str.isalnum       str.maketrans     str.translate
str.isalpha       str.partition     str.upper
str.isdecimal     str.replace       str.zfill
str.isdigit       str.rfind         

In [6]: str.capitalize('cat')
Out[6]: 'Cat'

In [7]: help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
```
* `capitalize`
* `title`
* `swapcase`
* `ljust`, `rjust`
* `upper`
* `lower`
* `isdigit`
* `zfill`
* `rfind`, `lfind`
* `strip`
* `index`, `find`
* `replace`
* `join`
* `partition`, `rpartition`
```
$ ipython3 -i unmagic.py
Python 3.4.2 (default, Jul  9 2015, 17:24:30) 
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: str.upper('cat')
Out[1]: 'CAT'

In [2]: 'cat'.upper()
Out[2]: 'CAT'

```
### Integer
```
$ ipython3 -i unmagic.py
Python 3.4.2 (default, Jul  9 2015, 17:24:30) 
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: type(5)
Out[1]: int

In [2]: type(6 + 3)
Out[2]: int

In [3]: int.
int.bit_length   int.from_bytes   int.real
int.conjugate    int.imag         int.to_bytes
int.denominator  int.numerator    

In [3]: bin(9)
Out[3]: '0b1001'

In [4]: int.bit_length(9)
Out[4]: 4

In [5]: x = 9

In [6]: x.bit_length()
Out[6]: 4

In [7]: 9.bit_length()
  File "<ipython-input-7-b579d6975e70>", line 1
    9.bit_length()
               ^
SyntaxError: invalid syntax

In [7]:
```
### Boolean
```
$ ipython3 -i unmagic.py
Python 3.4.2 (default, Jul  9 2015, 17:24:30) 
Type "copyright", "credits" or "license" for more information.

IPython 4.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 

In [1]: True
Out[1]: True

In [2]: False
Out[2]: False

In [3]: 1 == 1
Out[3]: True

In [4]: 1 == 3
Out[4]: False

In [5]: any([1 == 1, 1 == 3])
Out[5]: True

In [6]: all([1 == 1, 1 == 3])
Out[6]: False

In [7]: all([True, True, True])
Out[7]: True

In [8]: not True
Out[8]: False

In [9]: not False
Out[9]: True

In [10]: type(True)
Out[10]: bool

In [11]: bool.
bool.bit_length   bool.from_bytes   bool.real
bool.conjugate    bool.imag         bool.to_bytes
bool.denominator  bool.numerator    

In [11]: issubclass(bool, int)
Out[11]: True

In [12]: not 1
Out[12]: False

In [13]: not 0
Out[13]: True

In [14]: (True / 5) ** (True + 4)
Out[14]: 0.0003200000000000001

In [15]: 
```
### Float
```
>>> type(5.5)
<class 'float'>
>>> float.mro()
[<class 'float'>, <class 'object'>]
>>> float.
┌──────────────────────────────────────────────────────────────────────────────────┐
│ as_integer_ratio       conjugate              fromhex                            │
│ hex                    imag                   is_integer                         │
│ mro                    real                                                      │
└──────────────────────────────────────────────────────────────────────────────────┘
>>> 1/3
0.3333333333333333
>>> type(1/3)
<class 'float'>
>>> type(1)
<class 'int'>
>>> type(3)
<class 'int'>
>>> type(1/3)
<class 'float'>
>>> float.as_integer_ratio(1/3)
(6004799503160661, 18014398509481984)
>>> 6004799503160661/1801439850948198
0.3333333333333333
```
### [List](https://docs.python.org/3/tutorial/datastructures.html#lists)
List is our first complex data type. A list is an ordered collection of elements.
```
$ bpython
bpython version 0.14.2 on top of Python 2.7.8 /usr/bin/python2
>>> lx = list()
>>> lx
[]
>>> print(type(lx))
<type 'list'>
>>> li = [3, 3, 3]
>>> print(type(li))
<type 'list'>
>>> print(li)
[3, 3, 3]
>>> lj = [4, 5, 6, 7, 8]
>>> print(li + lj)
[3, 3, 3, 4, 5, 6, 7, 8]
>>> print(lj + li)
[4, 5, 6, 7, 8, 3, 3, 3]
>>> print(li,lj)
([3, 3, 3], [4, 5, 6, 7, 8])
>>> lk = ['cat', 'dog', 'elephant', 'pig']
>>> print(lk + li)
['cat', 'dog', 'elephant', 'pig', 3, 3, 3]
>>> lm = lk + lj
>>> print(lm)
['cat', 'dog', 'elephant', 'pig', 4, 5, 6, 7, 8]
>>> lm.append('jupiter')
>>> lj
[4, 5, 6, 7, 8]
>>> lm
['cat', 'dog', 'elephant', 'pig', 4, 5, 6, 7, 8, 'jupiter']
>>> lm[1]
'dog'
>>> lm[0]
'cat'
>>> lm[-1]
'jupiter'
>>> lm[10]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range
>>> lm[-10]
'cat'
>>> lm[-11]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range
>>> lm.
┌──────────────────────────────────────────────────────────┐
│ append     count      extend     index      insert       │
│ pop        remove     reverse    sort                    │
└──────────────────────────────────────────────────────────┘
>>> lm == lm
True
>>> lm is lm
True
>>> li
[3, 3, 3]
>>> li == [3, 3, 3]
True
>>> li is [3, 3, 3]
False
>>> 4 is 4
True
>>>
```

### [Set](https://docs.python.org/3/tutorial/datastructures.html#sets)
Sets are mutable unordered collections with fast lookup.
```
>>> li = list(range(200000000))
>>> si = set(li)
>>> value = li[-1]
>>> value
199999999
>>> value in li
True
>>> value in si
True
```
```
>>> li = ['pig', 'elephant', 345]
>>> si = set(li)
>>> print(si)
{345, 'pig', 'elephant'}
>>> si.add('olympia')
>>> si
{'olympia', 345, 'pig', 'elephant'}
```

### [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
```python
d = dict()
d['a'] = 'apple'
d['b'] = 'baboon'
d[1] = 'one'

```

For more information, checkout my [videos](https://www.youtube.com/watch?v=rtwAG8EdgDE&index=2&list=PL96V6k-MWWMhAXQmH0AJDKM6WnfpaCx4S) on dictionaries if you need more information. This is about 30 minutes of content going from introductory to advanced use of dictionaries. My environment is a little different, so print statements may show up differently than you are used to.

### Tuple and collections.namedtuple
tuples are immutable ordered collections
```
pos = (10, 20)
print(pos)
print(pos[0])
print(pos[1])

pos

Position = namedtuple('Position', ['x', 'y'])
pos = Position(10, 20)
print(pos)
```
## Control Flow
### if, elif and else, ternary
```
$ bpython
bpython version 0.15 on top of Python 3.4.2 /usr/bin/python3
>>> if 1 == 1:
...     print("cat")
...
cat
>>> if 1 == 3:
...     print("cat")
... else:
...     print("dog")
...
dog
>>> print("cat" if 1 == 1 else "dog")
cat
>>> print("cat" if 1 == 3 else "dog")
dog
>>> if 0:
...     print("0 equals true")
... elif 1:
...     print("1 equals true")
...
1 equals true
```
### Loops - For, While, Break, Continue
Loops are a code structure we use to identify repeated tasks. There are two major types of loops. `for` loops and `while` loops.

```python
#!/usr/bin/env python

iterable = [0, 10, -2, 3, 4]
for element in iterable:
    print(element)

iterable = {0, 10, -2, 3, 4}
for element in iterable:
    print(element)

iterable = {0:'zero', 10:'ten', -2:'negative two', 3:'three', 4:'four'}
for element in iterable:
    print(element)

for element in iterable:
    print('at key "{key}", value "{value}" is stored.'.format(key=element, value=iterable[element]))
```

```python
#!/usr/bin/env python

print('program start')
_ = input()
i = 0
while i < 10:
    print(i)
    i = i + 1


_ = input()
while i > 0:
    print(i)
    i = i - 1

_ = input()
while False:
    print('This will never print')

_ = input()
while True:
    print('This will print forever')

```
It is important to also understand flow in loops.

```python
#!/usr/bin/env python


_ = input('... pause ...')
iterable = [0, 10, -1, 3, 4]
for element in iterable:
    print(element)
    if element < 0:
        break # is like stop


_ = input('... pause ...')
for index, element in enumerate(iterable):
    if index > 3:
        break
    print(element):


_ = input('... pause ...')
for element in iterable:
    if element > 5:
        continue # is like ignore everything after this
    print(element)


_ = input('... pause ...')
for element in iterable:
    print(element)
    continue # has nothing to ignore


_ = input('... pause ...')
while True:
    text = input()
    if not text:
        break
    print(text)
```

## Rot 13
Your assignment is to write a ROT13 encoder. You should take as input a text string, then print a ROT13 encoded copy of the message

```python
#!/usr/bin/env python

original_message = input('what message would you like encoded')
for character in original_message:
    ...
...
```

## Boolean Games
- Conditional Logic/Booleans
 - Boolean quiz at [boolgame.py](./example-files/boolgame.py)
 - I usually have students make a program that will sort things from a list into other lists depending on the datatype or something along those lines
