import sys
input = sys.stdin.readline
N, M = map(int, input().split())
siteDict = dict()
for _ in range(N):
    site, password = input().split()
    siteDict[site] = password

for _ in range(M):
    print(siteDict.get(input().rstrip()))

