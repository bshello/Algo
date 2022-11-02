N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]
meet.sort(key=lambda x:(x[1], x[0]))
ans = 0
end = 0

for i in range(N):
    if meet[i][0] >= end:
        ans += 1
        end = meet[i][1]
print(ans)