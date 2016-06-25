#!/usr/bin/env python3

original_message = input ('what message would you like encoded ?' )

split_message = list(original_message)
new_message = []

for index, character in enumerate(split_message):
    # print(index, character)
    # a to m
    if (ord(character) < 111):
        #new_message[index] = chr(ord(character)+13)
        tmp =  chr(ord(character)+13)
        new_message.append(tmp)
    # n to z
    # else (ord(character) < 122):
    else:
        #new_message[index] = chr(ord(character)-13)
        new_message.append(chr(ord(character)-13))
print(''.join(split_message))
print(''.join(new_message))
