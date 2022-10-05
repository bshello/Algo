def solve(x, s, e):
    global ans
    while s <= e:
        mid = (s + e) // 2
        if x > arr_n[mid]:
            s = mid + 1
        elif x < arr_n[mid]:
            e = mid - 1
        else:
            ans = 1
            break
    return print(ans)





n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
arr_n.sort()
for i in arr_m:
    ans = 0
    solve(i, 0, n - 1)
