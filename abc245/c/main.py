import sys

input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo = [set() for _ in range(n)]

for i in range(n):
    for c in list(set([A[i], B[i]])):
        if i == 0:
            memo[i].add(c)
            continue
        for p_num in memo[i - 1]:
            diff = abs(p_num - c)
            if diff <= k:
                memo[i].add(c)


if len(memo[-1]) == 0:
    print('No')
else:
    print('Yes')
