# Introduction to Computer Programming
This is a course using python3.x, pip3, atom

## Overall Goals
1.	Give attendees a basic foundation to launch their learning journey (ex. Setting up environment)
2.	Vet students who have applied to bootcamp
3.	Create an opportunity for students to decide if programming is for them
4.	Market Code Guild

## Day 1
 - Get right version of python installed
 - Get atom installed
 - Teach basic command line (Most students will have never used or seen Bash/PowerShell)
 - Python
    * Variables
    * Strings
    * print()
    * String concatenation
    * String method .format()
    * Input()
 - Have the students make a Madlib.
 - Example File:
    * [/example-files/madlib.py](https://github.com/PdxCodeGuild/Intro-to-Computer-Programming/blob/master/example-files/madlib.py)

# Day 2
 - Other Data Types
    * Integers, Floats, Lists, Tuples and Dictionaries
 - Loops
    * for
    * while
 - Conditional Logic/Booleans
 - Boolean quiz at [/example-files/boolgame.py](https://github.com/PdxCodeGuild/Intro-to-Computer-Programming/blob/master/example-files/boolgame.py)
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
 