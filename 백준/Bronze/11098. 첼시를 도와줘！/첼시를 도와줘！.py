T = int(input())
for tc in range(T):
    n = int(input())
    lst = list()
    best = 0

    for i in range(n):
        a = list(input().split())
        lst.append(a)

    for j in range(len(lst)):
        if int(lst[j][0]) > best:
            best = int(lst[j][0])

    for k in range(len(lst)):
        if int(lst[k][0]) == best:
            break

    print(lst[k][1])