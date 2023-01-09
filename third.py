import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())


words = [input() for i in range(n)]

if words:
    w = max(max(map(len, words)), 4)
else:
    w = 4

print(" _____"+(w-1)*'_')
print("/  _\\ "+(w-1)*" "+"\\")
print("\\_/__\\"+(w-1)*" "+" \\")

for word in words:
    print("     |"+word.ljust(w)+'|')


print("     |   "+(w-4)*"_"+"_|___")
print("      \\ /__\\"+(w-2)*" "+"\\")
print("       \\___/"+(w-2)*"_"+"/")
