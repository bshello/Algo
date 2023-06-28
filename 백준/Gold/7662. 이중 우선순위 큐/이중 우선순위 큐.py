import sys
import heapq

T = int(input())
for _ in range(T):
    K = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * K
    for i in range(K):
        oper, num = input().split()
        num = int(num)
        if oper == "I":
            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))
            visited[i] = True
        else:
            if num == 1:
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

    ans = []
    while max_heap:
        tmp = heapq.heappop(max_heap)
        if visited[tmp[1]]:
            ans.append(-tmp[0])
            break

    while min_heap:
        tmp = heapq.heappop(min_heap)
        if visited[tmp[1]]:
            ans.append((tmp[0]))
            break

    if ans:
        print(ans[0], ans[1])
    else:
        print("EMPTY")