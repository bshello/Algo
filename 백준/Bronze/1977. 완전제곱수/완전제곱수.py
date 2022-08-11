m = int(input())
n = int(input())
num = list()
s = 0
nums = list()
for i in range(m, n+1):
    num.append(i)

for j in range(int(m**(1/2)), int(n**(1/2))+1):
    if j**2 in num:
        s += j**2
        nums.append(j**2)

if s == 0 or len(nums) == 0:
    print("-1")
else:
    print(s)
    print(nums[0])