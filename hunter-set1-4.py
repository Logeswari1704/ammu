# Hunter Set 1 Problem 4

import functools as f

n = int(input())
nums = list(map(int, input().split()))

sol = f.reduce(lambda x, y: x ^ y, nums)

print(sol)
