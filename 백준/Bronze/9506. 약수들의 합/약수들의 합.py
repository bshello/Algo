n = int(input())
while n!= -1:
    num = []
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            num.append(i)
    for j in num:
        sum += j
    exp = '1'
    nums = list(map(str, num))
    for k in range(1 , len(nums)-1):
        exp = exp + ' + ' + nums[k]
    if sum-n == n:
        print(f'{n} = {exp}')
    else:
        print(f'{n} is NOT perfect.')
    n = int(input())
