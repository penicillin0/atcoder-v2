import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
XK = [list(map(int, input().split())) for _ in range(Q)]


appear_map = {}
for i in range(N):
    a = A[i]
    if a not in appear_map:
        appear_map[a] = [i]
    else:
        appear_map[a].append(i)

for x, k in XK:
    if x not in appear_map:
        print(-1)
    else:
        if k - 1 >= len(appear_map[x]):
            print(-1)
        else:
            print(appear_map[x][k - 1] + 1)
