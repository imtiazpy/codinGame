# This is a shortest mode challenge:

# This solution is not the shortest, Try solving it with less character

s=input()
n=''
for i in s:
    if i.isalpha():
        if i.isupper():
            n+=i
            n+=i.lower()
        else:
            n+=i
            n+=i.upper()
    else:
        n+=i
print(n)
