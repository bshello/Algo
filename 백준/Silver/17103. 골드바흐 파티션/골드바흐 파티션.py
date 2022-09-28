import sys
input=sys.stdin.readline

arr = [True] * (1000001)
for i in range(2, 1000001):
    if arr[i] == True:
        for j in range(2 * i, 1000001, i):
            arr[j] = False

for tc in range(int(input())):
    N = int(input())
    cnt = 0
    for i in range(2, (N//2)+1):
        if arr[i] and arr[N-i]:
            cnt += 1

    print(cnt)