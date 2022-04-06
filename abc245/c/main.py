import sys

input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo = [set() for _ in range(n)]

for i in range(n):
    candidate = [A[i],  B[i]]
    for c in candidate:
        if i == 0:
            memo[i].add((c, True))
            continue
        for p_num, p_is in memo[i - 1]:
            if p_is is True:
                diff = abs(p_num - c)
                if diff <= k:
                    memo[i].add((c, True))


if len(memo[-1]) == 0:
    print('No')
else:
    print('Yes')
