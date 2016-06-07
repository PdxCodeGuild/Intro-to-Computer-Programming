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

def func(x, fund):
    return x + fund(x)

def fune(x):
    return x ** 2

print(func(5, fune))
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

 - Review dictionary methods
 - [Phone book challenge](./example-files/phonebook.py) – Have students make a phonebook program that will give the user a menu and have the capability to search, add, change and remove entries.
