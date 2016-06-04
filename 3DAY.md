# Day 3
### Functions
```python
#!/usr/bin/env python

def example_one():
    pass

def example_two():
    return 5

def example_three(x):
    return x
```
```python
#!/usr/bin/env python

x = 7

def example_four(x):
    return x + x

example_four(3)
```
```python
#!/usr/bin/env python

def example_five(x, y):
    return x + y

def example_six(x):
    def example_five(x, y):
        return x * y

    return example_five(x, x)
```
 - Review dictionary methods
 - [Phone book challenge](./example-files/phonebook.py) – Have students make a phonebook program that will give the user a menu and have the capability to search, add, change and remove entries.
