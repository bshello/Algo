k, n = map(int, input().split())
arr = [0] * k
for i in range(k):
    arr[i] = int(input())

s, e = 1, max(arr)
ans = 0
while s <= e:
    tmp = 0
    mid = (s + e) // 2
    for j in arr:
        tmp += j // mid
    if tmp >= n:
        ans = max(ans, mid)
        s = mid + 1
    elif tmp < n:
        e = mid - 1
    else:
        ans = max(ans, mid)
        break
print(ans)