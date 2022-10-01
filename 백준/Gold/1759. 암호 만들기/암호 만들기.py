def dfs(conso, vowel, password):
    if len(password) == N:
        if vowel > 0 and conso > 1:
            print(password)
        return

    for i in range(M):
        if not visited[i]:
            if len(password) == 0:
                visited[i] = 1
                if word[i] in vow:
                    dfs(conso, vowel + 1, password + word[i])
                else:
                    dfs(conso + 1, vowel, password + word[i])
                visited[i] = 0
            else:
                if password[-1] < word[i]:
                    visited[i] = 1
                    if word[i] in vow:
                        dfs(conso, vowel + 1, password + word[i])
                    else:
                        dfs(conso + 1, vowel, password + word[i])
                    visited[i] = 0

vow = ['a', 'e', 'i', 'o', 'u']
N, M = map(int, input().split())
word = list(input().split())
word.sort()
visited = [0] * M
dfs(0, 0, '')