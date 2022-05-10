import sys

input = sys.stdin.readline

n = int(input())
S = [str(input()) for _ in range(n)]


S_set = set(S)
for s in S:
    if s in S_set and '!' + s in S_set:
        print(s)
        exit()
print('satisfiable')
