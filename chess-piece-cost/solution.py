s = input()

price = {'Q': 9, 'K': 4, 'B':3, 'N': 3, 'P': 1, 'R': 5}

total = 0
for i in s:
    total += price[i]

if 'K' in s:
    print(total*200)
else:
    print(total*100)