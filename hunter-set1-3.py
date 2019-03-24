# Hunter Set 1 Problem 3

n = int(input())
nums = list(map(int, input().split()))

out = []

for i in range(n):
    if nums[i] == i:
        out.append(i)

if out:
    out = sorted(out)
    print(*out)
else:
    print('-1')
