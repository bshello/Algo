import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(c):

    if c == parent[c]: #루트노드 출력, 부모찾기
        return c
    parent[c] = find(parent[c])
    return parent[c]

def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return

N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]

for i in range(N):
    travel = list(map(int, input().split()))
    for j in range(len(travel)):
        if travel[j]:
            a = i + 1
            b = j + 1
            union(a, b)

plan = list(map(int, input().split()))
answer = "YES"
ans = find(plan.pop())
while plan:
    tmp = find(plan.pop())
    if ans != tmp:
        answer = "NO"
        break

print(answer)



