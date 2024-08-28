size = int(input())
array = [int(i) for i in input().rsplit(" ")]
moves = 0
for i in range(size - 1):
    if array[i+1] < array[i]: 
        moves += array[i] - array[i+1]
        array[i+1] += array[i] - array[i+1]
print(moves)