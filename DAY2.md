# Day 2 - Introduction to Types and Control Flow
## [Primative types](https://docs.python.org/3.5/library/stdtypes.html) and Exploration of Types
In this section we develop a more complete understanding of types. In your career you will likely run into code that is confusing. Gere we gain the skills needed to better explore types.

### [String](https://docs.python.org/3.5/library/string.html)
```
$ bpython
bpython version 0.15 on top of Python 3.4.2 /usr/bin/python3
>>> type('c')
<class 'str'>
>>> "cat"
'cat'
>>> type('cat')
<class 'str'>
>>> 'cat' + 'dog'
'catdog'
>>> type('cat' + 'dog')
<class 'str'>
>>> str.
┌──────────────────────────────────────────────────────────────────────────────────┐
│ capitalize       casefold         center           count                         │
│ encode           endswith         expandtabs       find                          │
│ format           format_map       index            isalnum                       │
│ isalpha          isdecimal        isdigit          isidentifier                  │
│ islower          isnumeric        isprintable      isspace                       │
│ istitle          isupper          join             ljust                         │
│ lower            lstrip           maketrans        mro                           │
│ partition        replace          rfind            rindex                        │
│ rjust            rpartition       rsplit           rstrip                        │
│ split            splitlines       startswith       strip                         │
│ swapcase         title            translate        upper                         │
│ zfill                                                                            │
└──────────────────────────────────────────────────────────────────────────────────┘
>>> str.capitalize('cat')
'Cat'
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str
    
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.

>>> str.upper('cat')
'CAT'
>>> 'cat'.upper()
'CAT'
>>> '**** {} ****'.format(9)
'**** 9 ****'
>>> '**** {} ****'.format('grape')
'**** grape ****'
```
### Integer
```
$ bpython
bpython version 0.15 on top of Python 3.4.2 /usr/bin/python3
>>> type(5)
<class 'int'>
>>> type(6 + 3)
<class 'int'>
>>> int.
┌──────────────────────────────────────────────────────────────────────────────────┐
│ bit_length      conjugate       denominator     from_bytes                       │
│ imag            mro             numerator       real                             │
│ to_bytes                                                                         │
└──────────────────────────────────────────────────────────────────────────────────┘
>>> bin(9)
'0b1001'
>>> int.bit_length(9)
4
```
### Boolean
```
$ bpython
bpython version 0.15 on top of Python 3.4.2 /usr/bin/python3
>>> True
True
>>> False
False
>>> 1 == 1
True
>>> 1 == 3
False
>>> any((1 == 1, 1 == 3))
True
>>> all((True, True, False))
False
>>> any((True, False, False))
True
>>> not True
False
>>> not False
True
>>> bool.
┌──────────────────────────────────────────────────────────────────────────────────┐
│ bit_length       conjugate        denominator      from_bytes                    │
│ imag             mro              numerator        real                          │
│ to_bytes                                                                         │
└──────────────────────────────────────────────────────────────────────────────────┘
>>> issubclass(bool, int)
True
>>> bool.mro()
[<class 'bool'>, <class 'int'>, <class 'object'>]
>>> not 1
False
>>> not 0
True
>>>
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
### [Set](https://docs.python.org/3/tutorial/datastructures.html#sets)
### [Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
### Tuple and collections.namedtuple

## Control Flow
 - Loops
  - for
  - while

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
- Conditional Logic/Booleans
 - Boolean quiz at [boolgame.py](./example-files/boolgame.py)
 - I usually have students make a program that will sort things from a list into other lists depending on the datatype or something along those lines
