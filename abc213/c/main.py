import sys
from bisect import bisect_left
input = sys.stdin.readline

h, w, n = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]

a_set, b_set = set(), set()

for a, b in AB:
    a_set.add(a)
    b_set.add(b)

a_list = list(a_set)
b_list = list(b_set)

a_list.sort()
b_list.sort()


for i, ab in enumerate(AB):
    a, b = ab
    a_idx = bisect_left(a_list, a) + 1
    b_idx = bisect_left(b_list, b) + 1
    print(a_idx, b_idx)
