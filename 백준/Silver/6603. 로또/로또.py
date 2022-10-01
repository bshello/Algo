def dfs():
    if len(lotto) == 6:
        print(*lotto)
        return

    for i in range(1, inp[0] + 1):
        if not visited[i]:
            if len(lotto) >= 1:
                if inp[i] > lotto[-1]:
                    visited[i] = 1
                    lotto.append(inp[i])
                    dfs()
                    lotto.pop()
                    visited[i] = 0
            else:
                visited[i] = 1
                lotto.append(inp[i])
                dfs()
                lotto.pop()
                visited[i] = 0

while True:
    inp = list(map(int, input().split()))
    if inp == [0]:
        break
    lotto = []
    visited = [0] * (inp[0] + 1)
    ans = 0
    dfs()
    print()