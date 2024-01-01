#!/usr/bin/python3
# Get the number of rows for the tree
rows = input("Enter number of rows for the tree: ")

rows = int(rows)

spaces = rows - 1
hashes = 1
stump_spaces = rows - 1

while rows != 0:

    for i in range(spaces):
        print(' ', end="")

    for i in range(hashes):
        print('#', end="")

    print()

    spaces -= 1
    hashes += 2
    rows -= 1

for i in range(stump_spaces):
    print(' ', end="")

print("#")

