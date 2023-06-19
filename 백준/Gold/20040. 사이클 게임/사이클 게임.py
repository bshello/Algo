import sys
input = sys.stdin.readline

def find(x):

    if x == parent[x]:
        return x

    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(a, b):

    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
ans = 0
for j in range(m):
    s, e = map(int, input().split())
    if find(s) == find(e):
        ans = j + 1
        break
    union(s, e)

print(ans)