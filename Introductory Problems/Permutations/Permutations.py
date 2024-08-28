n = int(input())

if n == 1:
    print(1)
elif n > 1 and n < 4:
    print("NO SOLUTION")
else:
    for i in range(2, n - n % 2 + 1, 2):
        print(i, end=" ")
    for i in range(1, n + (n % 2 - 1) + 1, 2):
        print(i, end=" ")