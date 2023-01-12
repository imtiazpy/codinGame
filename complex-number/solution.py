n = int(input())

complex_nums = []
for _ in range(n):
    complex_nums.append(complex(input().replace('i', 'j')))

complex_sum = sum(complex_nums)

if complex_sum == 0:
    print('0+0i')
else:
    print(f'{complex_sum*complex_sum}'[1:-1].replace('j', 'i'))
