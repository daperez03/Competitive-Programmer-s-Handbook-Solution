n = int(input())
inputs = [int(i) for i in input().rsplit(" ")]
inputs.sort()
for i in range(n - 1):
    if i+1 != inputs[i]:
        print(i+1)
        exit()
print(n)