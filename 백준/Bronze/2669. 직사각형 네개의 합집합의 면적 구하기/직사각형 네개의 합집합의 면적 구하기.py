sql = list()
for _ in range(4):
    sq = list(map(int, input().split()))
    sql.append(sq)

arr = [[0]*100 for _ in range(100)]
ans = 0
for i in range(4):
    for j in range(sql[i][1], sql[i][3]):
        for k in range(sql[i][0], sql[i][2]):
            if arr[j][k] == 0:
                arr[j][k] = 1
                ans += 1
print(ans)