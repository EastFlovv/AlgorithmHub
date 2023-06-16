import sys

def get_input():
    return sys.stdin.readline().strip()

# 수의 갯수 n, 구간의 수 m
n, m = map(int, get_input().split(' '))

# a1 ~ an
nums = [0] + list(map(int, get_input().split(' ')))
acc = []

for i in range(n+1):
    if i > 0:
        acc.append(acc[i-1] + nums[i])
    else:
        acc.append(nums[0])

for _ in range(m):
    s, e = map(int, get_input().split(' '))
    print(acc[e] - acc[s-1])