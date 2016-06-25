original_message = input('what message would you like encoded')
split_message = list(original_message)
for index, element in enumerate(split_message):
   x=ord(element)-97+13
   y=(x%26)+97
   split_message[index]=chr(y)

print(''.join(split_message))
