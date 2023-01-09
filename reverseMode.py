s = input()

a = [ord(c.upper()) for c in s]
b = sum(a)//len(a)
print(chr(b))