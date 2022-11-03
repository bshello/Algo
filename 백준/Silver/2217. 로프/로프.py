N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)
ans = 0
for i in range(N):
    temp = rope[i] * (i + 1)
    ans = max(ans, temp)
print(ans)