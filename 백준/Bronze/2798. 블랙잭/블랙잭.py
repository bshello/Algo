def dfs(M, A, j):
    global ans
    if len(card) > 3:
        return
    if A > M:
        return

    if len(card) == 3 and ans < A:
        ans = A
        temp = ans

    for i in range(j, N):
        if not visited[i] and A + deck[i] <= M:
            visited[i] = 1
            card.append(deck[i])
            dfs(M, A + deck[i], i)
            card.pop()
            visited[i] = 0


N, M = map(int, input().split())
deck = list(map(int, input().split()))
deck.sort(reverse=True)
card = []
visited = [0] * N
ans = 0
dfs(M, 0, 0)
print(ans)