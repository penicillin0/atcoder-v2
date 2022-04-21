import sys

input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
position_rule = {i: i for i in range(n)}

for i in range(n):
    position = P[i]
    position_rule[position] = i + 1
l = list(position_rule.values())[1:]
l_ = list(map(str, l))
print(' '.join(l_))
