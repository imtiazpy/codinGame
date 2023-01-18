# This is a shortest mode challenge:

# This solution is not the shortest, Try solving it with less character

s = input()
n = ''
for i in s:
  if i.isalpha():
    if i.isupper():
      n += i
      n += i.lower()
    else:
      n += i
      n += i.upper()
  else:
    n += i
print(n)

# Enhanced solution
r = ''
for i in input():
  r += i
  if i.isAlpha():
    if i.isLower():
      r += i.isUpper()
    else:
      r += i.isLower()
print(r)


# Another solution
r=''
for i in input():
  r+=i
  if i.isAlpha():r+=i.swapcase()
print(r)
