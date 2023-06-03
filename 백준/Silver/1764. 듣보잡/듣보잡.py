import sys
input = sys.stdin.readline
N, M = map(int, input().split())

d = dict()
for _ in range(N):
    d[input().rstrip()] = 1
db = list()
for _ in range(M):
    name = input().rstrip()
    if name in d:
        db.append(name)
db.sort()

print(len(db))
for i in db:
    print(i)