import sys
sys.setrecursionlimit(10**5)

def find(c):

    if member[c] == c:
        return c

    p = find(member[c])
    member[c] = p
    return member[c]

def union(x, y):

    x = find(x)
    y = find(y)
    if x == y:
        return
    
    s = friendNum[x] + friendNum[y]

    if x < y:
        member[y] = x
        friendNum[x] = s
        friendNum[y] = s
        return
    else:
        member[x] = y
        friendNum[y] = s
        friendNum[x] = s
        return


T = int(input())
for _ in range(T):
    F = int(input())
    friend = dict()
    friendNum = dict()
    member = [0]
    count = 1
    for i in range(1, F + 1):
        a, b = input().split()
        if a not in friend:
            friend[a] = count
            friendNum[count] = 1
            member.append(count)
            count += 1
        if b not in friend:
            friend[b] = count
            friendNum[count] = 1
            member.append(count)
            count += 1
        tempa = friend[a]
        tempb = friend[b]
        union(tempa, tempb)
        print(friendNum[member[tempa]])