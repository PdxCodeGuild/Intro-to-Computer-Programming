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
```python
#!/usr/bin/env python

def func(x, fund):
    return x + fund(x)

def fune(x):
    return x ** 2

func(5, fune)
```
```python

#!/usr/bin/env python
def func(x):
    return x * x

li = [0, 1, 2, 3, 4, 5, 6, 7]

for index, value in enumerate(li):
    li[index] = func(value)

print(li)
```
```python
#!/usr/bin/env python

"""
'scope of a variable is defined at the level of assignment' -- Elana Hashman
"""

cat = 'meow'

def cat_changer():
    cat = 'purr'
    print('inside cat: ', cat)

cat_changer()
print('outside cat: ', cat)
```

 - Review dictionary methods
 - [Phone book challenge](./example-files/phonebook.py) – Have students make a phonebook program that will give the user a menu and have the capability to search, add, change and remove entries.
