import sys
input = sys.stdin.readline

N = int(input())
S = input()

ans = 0

x_cnt = []
o_cnt = []

# xのカウント
cnt = 0
for s in S:
    if s == 'x':
        cnt += 1
    else:
        x_cnt.append(cnt)
        cnt = 0

# oのカウント
cnt = 0
for s in S:
    if s == 'o':
        cnt += 1
    else:
        o_cnt.append(cnt)
        cnt = 0
# print('o_cnt', o_cnt)
# print('x_cnt', x_cnt)

rm_cnt = 0

for cnt in x_cnt:
    if 2 > cnt:
        continue

    rm_cnt += cnt * (cnt - 1) // 2


for cnt in o_cnt:
    if 2 > cnt:
        continue

    rm_cnt += cnt * (cnt - 1) // 2

print(N * (N - 1) // 2 - rm_cnt)
