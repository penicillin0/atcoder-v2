import sys
input = sys.stdin.readline

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]


ruiseki_1 = {-1: 0}
ruiseki_2 = {-1: 0}

amt_1, amt_2 = 0, 0

for i in range(N):
    c, p = CP[i]
    if c == 1:
        amt_1 += p
    else:
        amt_2 += p
    ruiseki_1[i] = amt_1
    ruiseki_2[i] = amt_2


for l, r in LR:
    print(ruiseki_1[r-1] - ruiseki_1[l-2], ruiseki_2[r-1] - ruiseki_2[l-2])
