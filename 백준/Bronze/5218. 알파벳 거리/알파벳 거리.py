alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

T = int(input())
for tc in range(T):
    n, m = map(str, input().split())

    tempal = list()
    tempn = list()

    for j in n:
        for k in range(len(alpha)):
            if j == alpha[k]:
                tempal.append(k)
    for x in m:
        for y in range(len(alpha)):
            if x == alpha[y]:
                tempn.append(y)
    ans = list()
    for z in range(len(n)):
        temp = 0
        temp = tempn[z] - tempal[z]
        if temp < 0:
            temp += 26
        ans.append(temp)

    print('Distances: ', end = '')
    for o in range(len(ans)):
        print(ans[o], end=' ')
    print('')