from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

bind_dict = {}

for i in range(1, N + 1):
    bind_dict[i] = []

for a, b in AB:
    bind_dict[a].append(b)
    bind_dict[b].append(a)

# 葉を探す
start_leaf = 0
for i in range(1, N + 1):
    if len(bind_dict[i]) == 1:
        start_leaf = i
        break

check = 1
check_board = {}
for i in range(1, N + 1):
    check_board[i] = 0

# DFS

# sys.setrecursionlimit(10 ** 6)

# def check_leaf(check, point, check_board: dict):
#     if check_board[point] != 0:
#         return
#     else:
#         check_board[point] = check
#         for i in bind_dict[point]:
#             check_leaf(check * -1, i, check_board)


# check_leaf(check, start_leaf, check_board)


# BFS
q = deque()
q.append(start_leaf)
check_board[start_leaf] = check
while q:
    if len(q) == 0:
        break
    point = q.popleft()
    for i in bind_dict[point]:
        if check_board[i] != 0:
            continue
        else:
            q.append(i)
            check_board[i] = check_board[point] * -1


ans_set = set()
for key, value in check_board.items():
    if value == 1:
        ans_set.add(key)

if len(ans_set) < N // 2:
    ans_set = set(range(1, N + 1)) - ans_set

print(*list(ans_set)[: N // 2])
