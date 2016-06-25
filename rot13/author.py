original_message = input('what message would you like encoded')
split_message = list(original_message)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
secret_alphabet = 'nopqrstuvwxyzabcdefghijklm'
for index, character in enumerate(split_message):
    if character.isalpha():
        x = alphabet.find (character)
        new_character = secret_alphabet [x]
    else:
        new_character = character
    print (new_character, end='')
