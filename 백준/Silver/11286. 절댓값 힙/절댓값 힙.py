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
            tmp = []
            while min_heap and min_heap[0][0] == min_absValue:
                tmp_absValue, tmp_realValue = heapq.heappop(min_heap)
                if tmp_realValue < min_realValue:
                    ans = tmp_realValue
                    heapq.heappush(tmp, (min_absValue, min_realValue))
                else:
                    heapq.heappush(tmp, (tmp_absValue, tmp_realValue))

            while tmp:
                tmp_absValue, tmp_realValue = heapq.heappop(tmp)
                heapq.heappush(min_heap, (tmp_absValue, tmp_realValue))

            print(ans)
        else:
            print(0)

