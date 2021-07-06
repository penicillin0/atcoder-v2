import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
B = [int(input()) for _ in range(Q)]

for b in B:
    left = bisect_left(A, b) - 1
    right = left + 1
    if right > n - 1:
        print(abs(b - A[left]))
    else:
        print(min(abs(b - A[left]), abs(b - A[right])))
