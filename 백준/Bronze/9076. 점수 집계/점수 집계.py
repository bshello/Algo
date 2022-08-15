T = int(input())
for tc in range(T):
    n = list(map(int, input().split()))
    n.sort()
    if n[-2] >= n[1]+4:
        print('KIN')
    else:
        s = 0
        for i in range(1,4):
            s+=n[i]
        print(s)