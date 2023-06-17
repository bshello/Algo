import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def find(c):
    if c == parent[c]: #루트노드 출력, 부모찾기
        return c

    p = find(parent[c])
    parent[c] = p
    return find(parent[c])

def union(x, y):

    a = find(x)
    b = find(y)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    return

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        d = find(a)
        f = find(b)
        if d != f:
            print("NO")
        else:
            print("YES")
