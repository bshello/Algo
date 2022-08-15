T = int(input())
N = 3
for tc in range(T):
    n = list(map(int, input().split()))
    n.sort()
    print(n[-N])