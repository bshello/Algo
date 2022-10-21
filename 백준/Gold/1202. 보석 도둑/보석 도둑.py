from heapq import heappop, heappush

# 입력값 받기
N, K = map(int,input().split())
jews = []
bags = []
for n in range(N):
    heappush(jews,tuple(map(int,input().split())))

for b in range(K):
    bags.append(int(input()))

bags.sort()

# 가방에 들어갈 수 있는 보석들 중에서 값어치가 큰 값을 찾아준다.
new_jews = []
result = 0
for bag in bags:
    while jews and jews[0][0] <= bag:
        M, V = heappop(jews)
        heappush(new_jews,(-V,M))

    # 만약에 new_jews가 없을 경우도 있으면? continue
    if not new_jews:
        continue

    # 아니면 결과값 더해주기
    V, M = heappop(new_jews)
    result -= V

print(result)



