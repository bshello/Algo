n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = 1
e = max(arr)
ans = 0
while s <= e:
    tmp = 0
    mid = (s + e) // 2

    for i in arr:
        if i > mid:
            tmp += i - mid

    if tmp >= m:
        ans = max(ans, mid)
        s = mid + 1
    elif tmp < m:
        e = mid - 1
    else:
        ans = max(ans, mid)
        break

print(ans)