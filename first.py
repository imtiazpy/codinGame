# print the number of occurence of a character in a string
# input banbacd
# output 1112211

s = input()

countDict = {}
output = []

for i in s:
    if i in countDict.keys():
        countDict[i] = countDict[i] + 1
        output.append(str(countDict[i]))
    else:
        countDict[i] = 1
        output.append(str(countDict[i]))

print(''.join(output))
