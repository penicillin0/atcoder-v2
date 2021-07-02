import sys
input = sys.stdin.readline

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

tate = []
yoko = []


for i in range(w):
    t = sum([A[j][i] for j in range(h)])
    tate.append(t)

for i in range(h):
    y = sum(A[i])
    yoko.append(y)


ans = []
for j in range(h):
    line = []
    for i in range(w):
        line.append(tate[i] + yoko[j] - A[j][i])
    ans.append(line)

for a in ans:
    print(*a)
