import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap = []

for i in range(N):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(min_heap, (abs(tmp), tmp))
    else:
        if min_heap:
            min_absValue, min_realValue = heapq.heappop(min_heap)
            ans = min_realValue
            print(ans)
        else:
            print(0)

