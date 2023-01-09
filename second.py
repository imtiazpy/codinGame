# print the sum of ASCII characters of a string multiplying with its index
s = input()
res = 0
for i in range(0, len(s)):
    res += ord(s[i]) * i
print(res)
