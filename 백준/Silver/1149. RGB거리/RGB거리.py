import sys

input = sys.stdin.readline
N = int(input())
ans = sys.maxsize
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))
dp = [[0] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = house[0][i]

for j in range(1, N):

    dp[j][0] = house[j][0] + min(dp[j - 1][1], dp[j - 1][2])
    dp[j][1] = house[j][1] + min(dp[j - 1][0], dp[j - 1][2])
    dp[j][2] = house[j][2] + min(dp[j - 1][0], dp[j - 1][1])

ans = min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2])
print(ans)