n = 100
pap = int(input())
arr = [[0] * n for _ in range(n)]
mar = 0
mac = 0
mic = 100
mir = 100
for _ in range(pap):
    c, r = map(int, input().split())
    for i in range(r, 10+r):
        for j in range(c, 10+c):
            arr[i][j] = 1
    if mar < r:
        mar = r
    if mac < c:
        mac = c
    if mir > r:
        mir = r
    if mic > c:
        mic = c

ans = 0
for i in range(mir, mar+10):
    for j in range(mic, mac+10):
        if arr[i][j] == 1:
            ans += 1

print(ans)