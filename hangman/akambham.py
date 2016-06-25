#!/usr/bin/env python2.7

word = "Basket Ball"
guessed_word = ['X','X','X','X','X','X',' ', 'X','X','X','X']
guessed = 1

while(guessed < len(word.strip(' '))):
 #print('guessed letters is ', guessed, 'and word len is ', len(word.strip()), ' ', word.strip())
 input = raw_input('Enter your next guess....')
 guess_char = input[0]

 count = word.count(guess_char)
 guessed += count

 start = 0;
 print(count, " instances of guessed char")

 for i in range(0, count):
   correct_index = word.find(guess_char, start)
   start = correct_index+1
   guessed_word[correct_index] = guess_char
 print("guessed word is ", guessed_word)
