n = int(input())

if n == 1:
    a = b = 1
elif n == 2:
    a = 1
    b = 2
else:
    for i in range(1, n):
        if n <= i:
            break
        n -= i

    if i % 2 == 1:
        b = n
        a = i + 1 - b

    else:
        a = n
        b = i + 1 - a



print(f'{a}/{b}')