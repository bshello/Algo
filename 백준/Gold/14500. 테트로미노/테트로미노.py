def tetro1(r, c):
    global ans
    temp = 0
    for k in range(4):
        dc = c + k
        temp += arr[r][dc]
    ans = max(ans, temp)
    return

def tetro2(r, c):
    global ans
    temp = 0
    for k in range(4):
        dr = r + k
        temp += arr[dr][c]
    ans = max(ans, temp)
    return

def tetro3(r, c):
    global ans
    temp = arr[r][c] + arr[r + 1][c] + arr[r][c + 1] + arr[r + 1][c + 1]
    ans = max(ans, temp)
    return

def tetro4(r, c):
    global ans
    temp1 = arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
    temp1 = max(temp1 + arr[r + 1][c], temp1 + arr[r + 1][c + 1], temp1 + arr[r + 1][c + 2])
    temp2 = arr[r + 1][c] + arr[r + 1][c + 1] + arr[r + 1][c + 2]
    temp2 = max(temp2 + arr[r][c], temp2 + arr[r][c + 1], temp2 + arr[r][c + 2])
    temp3 = 0
    for k in range(2):
        for l in range(3):
            temp3 +=arr[r + k][c + l]
    temp3 = max(temp3 - arr[r][c] - arr[r + 1][c + 2], temp3 - arr[r][c + 2] - arr[r + 1][c])
    ans = max(ans, temp1, temp2, temp3)
    return

def tetro5(r, c):
    global ans
    temp1 = arr[r][c] + arr[r + 1][c] + arr[r + 2][c]
    temp1 = max(temp1 + arr[r][c + 1], temp1 + arr[r + 1][c + 1], temp1 + arr[r + 2][c + 1])
    temp2 = arr[r][c + 1] + arr[r + 1][c + 1] + arr[r + 2][c + 1]
    temp2 = max(temp2 + arr[r][c], temp2 + arr[r + 1][c], temp2 + arr[r + 2][c])
    temp3 = 0
    for k in range(3):
        for l in range(2):
            temp3 +=arr[r + k][c + l]
    temp3 = max(temp3 - arr[r][c] - arr[r + 2][c + 1], temp3 - arr[r][c + 1] - arr[r + 2][c])
    ans = max(ans, temp1, temp2, temp3)
    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if M - j > 3:
            tetro1(i, j)
        if N - i > 3:
            tetro2(i, j)
        if N - i > 1 and M - j > 1:
            tetro3(i, j)
        if N - i > 1 and M - j > 2:
            tetro4(i, j)
        if N - i > 2 and M - j > 1:
            tetro5(i, j)

print(ans)