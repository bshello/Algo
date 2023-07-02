import sys
import heapq

input = sys.stdin.readline

def djikstra(start):
    global graph
    distances = [0xffffff for _ in range(len(graph))]
    distances[start] = 0
    Q = []
    heapq.heappush(Q, (distances[start], start))

    while Q:

        current_distance, current_destination = heapq.heappop(Q)
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(Q, (distance, new_destination))

    return distances




N, E = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))
v1, v2 = map(int, input().split())

basic_distance = djikstra(0)
v1_distance = djikstra(v1 - 1)
v2_distance = djikstra(v2 - 1)
ans = min(basic_distance[v1 - 1] + v1_distance[v2 - 1] + v2_distance[N - 1], basic_distance[v2 - 1] + v2_distance[v1 - 1] + v1_distance[N - 1])
if ans >= 0xffffff:
    ans = -1
print(ans)
