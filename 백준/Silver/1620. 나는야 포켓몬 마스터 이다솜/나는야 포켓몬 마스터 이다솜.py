import sys

N, M = map(int, input().split())

pocketList = []
pocketDict = dict()
for i in range(N):
    pocketmon = input()
    pocketList.append(pocketmon)
    pocketDict[pocketmon] = i

for _ in range(M):
    problem = input()
    if problem.isalpha():
        print(pocketDict.get(problem) + 1)
    else:
        print(pocketList[int(problem) - 1])