import sys

N, M = map(int, input().split())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())

arr.sort()
ans = sys.maxsize
s, e = 0, 1
# while s < N and e < N:
#     e = s + 1
#     while e < N:
#         res = arr[e] - arr[s]
#         if res > M and res < ans:
#             ans = res
#             break
#         elif res == M:
#             ans = res
#             break
#         e += 1
#     s += 1
#     if ans == res:
#         break

while s < N and e < N:
    res = arr[e] - arr[s]

    if res == M:
        ans = res
        break
    elif res < M:
        e += 1

    elif res > M:
        s += 1
        e = s + 1
        if res < ans:
            ans = res

print(ans)