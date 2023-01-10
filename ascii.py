# You have space-separated 10 strings n.
# Each string of n is either a number or a letter in upper or lower case. You need to replace letters with their ASCII-codes and numbers with corresponding letter from the ASCII table.

n = input()

print([ord(c) if c.isalpha() else chr(int(c)) for c in n.split()])