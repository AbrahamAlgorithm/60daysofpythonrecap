#!/usr/bin/python3
message = input("Enter your message: ")
key = int(input("How many chars should we shift: ")

#prepare secret_message

secret_message=" "

for char in message:
if char.isalpha():
char_code = ord(char)
char_code += key

if char.isupper():

if char_code > ord('Z'):
char_code = 26

if char_code < ord('A')
char_code += 26

else:
if char_code > ord('z'):
char_code = 26

if char_code < ord('a')
char_code += 26

secret_message += chr(char_code)
else:
secret_message += char

print("Encrypted :", secret_message)

key = -key
org_message =" "

for char in message:
if char.isalpha():
char_code = ord(char)
char_code += key

if char.isupper():

if char_code > ord('Z'):
char_code = 26

if char_code < ord('A')
char_code += 26

else:
if char_code > ord('z'):
char_code = 26

if char_code < ord('a')
char_code += 26

secret_message += chr(char_code)
else:
    secret_message += char

    print("Encrypted :", secret_message)

    key = -key
    org_message =" "
