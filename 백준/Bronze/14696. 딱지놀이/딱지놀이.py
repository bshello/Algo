n = int(input())
for _ in range(n):
    ad = {4: 0, 3: 0, 2: 0, 1: 0}
    bd = {4: 0, 3: 0, 2: 0, 1: 0}
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, len(a)):
        ad[a[i]] += 1
    for j in range(1, len(b)):
        bd[b[j]] += 1

    if ad[4] > bd[4]:
        ans = 'A'
    elif ad[4] < bd[4]:
        ans = 'B'
    else:
        if ad[3] > bd[3]:
            ans = 'A'
        elif ad[3] < bd[3]:
            ans = 'B'
        else:
            if ad[2] > bd[2]:
                ans = 'A'
            elif ad[2] < bd[2]:
                ans = 'B'
            else:
                if ad[1] > bd[1]:
                    ans = 'A'
                elif ad[1] < bd[1]:
                    ans = 'B'
                else:
                    ans = 'D'
    print(ans)
