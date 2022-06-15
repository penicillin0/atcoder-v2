import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))

X = [int(input()) for _ in range(q)]


A.sort()

for x in X:
    point = bisect_left(A, x)
    print(len(A) - point)
