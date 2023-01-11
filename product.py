# reverse mode 
# input:
# 3
# Juice
# TV
# TV
# 5
# Jack 10
# TV 2000
# Juice 10
# Apple 4
# Fax 90

# output: 4010

# write suitable code

n = int(input())
a=0
l=[]
for i in range(n):
    l += [input()]
c = int(input())
for i in range(c):
    inputs = input().split()
    item = inputs[0]
    cost = int(inputs[1])
    for i2 in l:
        if i2==item:
            a+=cost

print(a)


