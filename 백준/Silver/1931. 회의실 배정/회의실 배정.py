import sys

input = sys.stdin.readline
N = int(input())

meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))

meetings.sort(key=lambda x: (x[0], x[1]))

end_time = 0
ans = 0
for meeting in meetings:

    if meeting[1] >= end_time:
        end_time = meeting[0]
        ans += 1
print(ans)