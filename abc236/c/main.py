import sys

input = sys.stdin.readline
n, m = map(int, input().split())
S = list(map(str, input().split()))
T_set = set(list(map(str, input().split())))

for s in S:
    print("Yes" if s in T_set else "No")
