import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

odd = []
even = []

for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

candidate = []

odd.sort()
even.sort()

if len(odd) >= 2:
    candidate.append(odd[-1] + odd[-2])


if len(even) >= 2:
    candidate.append(even[-1] + even[-2])


if len(candidate) == 0:
    print(-1)
    exit()

print(max(candidate))
