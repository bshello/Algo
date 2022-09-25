n = list(map(int, list(input())))
if sum(n) % 3 != 0 or 0 not in n:
    print(-1)
else:
    n.sort(reverse=True)
    for i in n:
        print(i, end='')

