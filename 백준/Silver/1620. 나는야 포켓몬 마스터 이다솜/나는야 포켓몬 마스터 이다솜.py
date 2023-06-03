import sys
input = sys.stdin.readline
N, M = map(int, input().split())

pocketList = []
pocketDict = dict()
for i in range(N):
    pocketmon = input().rstrip()
    pocketList.append(pocketmon)
    pocketDict[pocketmon] = i

for _ in range(M):
    problem = input().rstrip()
    if problem.isalpha():
        print(pocketDict.get(problem) + 1)
    else:
        print(pocketList[int(problem) - 1])