inpt = input()
count = 0
maxLen = 0
previous = ''

for i in inpt:
    if previous != i:
        previous = i
        count = 0
    count += 1
    if maxLen < count : maxLen = count

print(maxLen)