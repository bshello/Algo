n, m = map(int, input().split())
rm = m
rn = n
k = int(input())
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
r = m - 1
j = c = 0
i = x = y = 1
arr = [[0]*n for _ in range(m)]
ansr = r
ansc = c

if k > n*m:
    print(0)
else:
    while i < k+1:
        arr[r][c] = i
        if j == 0 or j == 2:
            if x == m:
                x = 0
                m -= 1
                j += 1
            x += 1

        else:
            if y == n-1:
                y = 0
                n -= 1
                j += 1
                if j == 4:
                    j = 0
            y += 1

        ansr = r
        ansc = c
        r += dr[j]
        c += dc[j]
        i += 1
        if i > rn * rm:
            break
            
    print(ansc+1, rm - ansr)
