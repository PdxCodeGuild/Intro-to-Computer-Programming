# Introduction to Computer Programming
This is a course using python3.x, pip3, atom

## Overall Goals
1. Give attendees a basic foundation to launch their learning journey (ex. Setting up environment)
2. Vet students who have applied to bootcamp
3. Create an opportunity for students to decide if programming is for them
4. Market Code Guild

## Day 1
- Get right version of python installed
- Get atom installed
- Teach basic command line (Most students will have never used or seen Bash/PowerShell)
- Python
 - Variables
 - Using Strings
 - print()
 - String concatenation
 - String method .format()
 - Input()
- Have the students make a Madlib.
 - Example File: [madlib.py](./example-files/madlib.py)

## Day 2
### [Primative types](https://docs.python.org/3.5/library/stdtypes.html)
 - List
 - Dictionary
 - Tuples and collections.namedtuple

#### [String](https://docs.python.org/3.5/library/string.html)
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
#### Integer
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
#### Boolean
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
#### Float
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
>>> _[0] / _[1]
0.3333333333333333
```

### Control Flow
 - Loops
  - for
  - while

#### if, elif and else, ternary
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
 - Boolean quiz at [/example-files/boolgame.py](./example-files/boolgame.py)
 - I usually have students make a program that will sort things from a list into other lists depending on the datatype or something along those lines

# Day 3
 - Functions
 - Review dictionary methods
 - Phone book challenge – Have students make a phonebook program that will give the user a menu and have the capability to search, add, change and remove entries.
    * [/example-files/phonebook.py](https://github.com/PdxCodeGuild/Intro-to-Computer-Programming/blob/master/example-files/phonebook.py)

# Day 4
 - Python Modules
    * Pip

# Day 5
 - Classes
 - Have students remake the phone book or another thing they did as a class
 - I usually use this example to explain classes and inheritance.

Suppose we want to model a bank account with support for deposit and withdraw operations. One way to do that is by using global state as shown in the following example.
```python
balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance
```
The above example is good enough only if we want to have just a single account. Things start getting complicated if want to model multiple accounts.

We can solve the problem by making the state local, probably by using a dictionary to store the state.
```python
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']
```
With this it is possible to work with multiple accounts at the same time.
```python
>>> a = make_account()
>>> b = make_account()
>>> deposit(a, 100)
100
>>> deposit(b, 50)
50
>>> withdraw(b, 10)
40
>>> withdraw(a, 10)
90
```
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
```
```python
>>> a = BankAccount()
>>> b = BankAccount()
>>> a.deposit(100)
100
>>> b.deposit(50)
50
>>> b.withdraw(10)
40
>>> a.withdraw(10)
90
```
### Inheritance
Let us try to create a little more sophisticated account type where the account holder has to maintain a pre-determined minimum balance.
```python
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
```


# Day 6
 - I normally don’t have anything set for day 6 because the other days will eat into this.
 
