#!/usr/bin/env python3

original_message = input('what message would you like encoded? ')
split_message = list(original_message)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
secret   = 'nopqrstuvwkyzabcdefghijklm'
lookup   = dict(zip(alphabet, secret))

for index, character in enumerate(split_message):
    if not character.isalpha():
        continue
    
    split_message[index] = lookup[character.lower()]
    if character.isupper():
  split_message[index] = split_message[index].upper()

print(''.join(split_message))

