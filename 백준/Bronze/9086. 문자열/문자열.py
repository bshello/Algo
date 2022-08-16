T = int(input())
for tc in range(T):
    n = list(input())
    ans = list()
    ans.append(n[0])
    ans.append(n[-1])
    answer = ''.join(ans)
    print(answer)