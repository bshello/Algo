import sys

def solve(N, start_x, start_y):
    global r, c, ans

    if N == 0:
        return

    border_x = start_x + 2**(N - 1)
    border_y = start_y + 2**(N - 1)

    if r >= border_x and c >= border_y:
        tmp = 4
        ans += 2**(2 * N - 2) * 3
        solve(N - 1, border_x, border_y)
    elif r >= border_x and c < border_y:
        tmp = 3
        ans += 2**(2 * N - 2) * 2
        solve(N - 1, border_x, start_y)
    elif r < border_x and c >= border_y:
        tmp = 2
        ans += 2**(2 * N - 2) * 1
        solve(N - 1, start_x, border_y)
    else:
        tmp = 1
        ans += 2**(2 * N - 2) * 0
        solve(N - 1, start_x, start_y)

    return


input = sys.stdin.readline
N, r, c = map(int, input().split())
ans = 0
solve(N, 0, 0)

print(ans)