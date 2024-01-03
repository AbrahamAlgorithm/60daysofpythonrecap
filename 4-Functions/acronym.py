#!/usr/bin/python3
string = input("Input the name you want to convert to acronymn: ")

string = string.upper()
#convert strinf to list
list_of_words = string.split()

for word in list_of_words:
    print(word[0], end=" ")

print()
