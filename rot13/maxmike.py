# Python Rot13 Program
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
crypt = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
convert = str.maketrans(alpha,crypt)
print(convert)
plaintext = input("What is the message, Caesar? ")
print (plaintext.translate(convert))
