# Day 2 - Introduction to Types and Control Flow
## [Primitive types](https://docs.python.org/3.5/library/stdtypes.html) and Exploration of Types
In this section we develop a more complete understanding of types. In your career you will likely run into code that is confusing. Here we gain the skills needed to better explore types.

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
>>> (True/5)**(True + 4)
0.0003200000000000001
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
Sets are unordered but faster.
```
>>> *li,  = range(200000000)
>>> si    = set(li)
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
1.
2. Check out my [videos](https://www.youtube.com/watch?v=rtwAG8EdgDE&index=2&list=PL96V6k-MWWMhAXQmH0AJDKM6WnfpaCx4S) on dictionaries if you need more information. This is about 30 minutes of content going from introductory to advanced use of dictionaries. My environment is a little different, so print statements may show up differently than you are used to.

### Tuple and collections.namedtuple

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

- Conditional Logic/Booleans
 - Boolean quiz at [boolgame.py](./example-files/boolgame.py)
 - I usually have students make a program that will sort things from a list into other lists depending on the datatype or something along those lines
