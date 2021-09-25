import sys


def main():
    from builtins import input, int, map
    input = sys.stdin.readline

    N = int(input())
    LINE_NUM = 1001

    mai_cnt = {}

    for i in range(N + 1):
        mai_cnt[i] = 0

    line_start_end = {}

    # j行目
    for j in range(LINE_NUM):
        line_start_end[j] = [0 for _ in range(LINE_NUM + 1)]

    # i枚目
    for i in range(N):
        a, b, c, d = map(int, input().split())
        # j行目
        for j in range(b, d):
            line_start_end[j][a] += 1
            line_start_end[j][c] -= 1

    for i in range(LINE_NUM):
        cnt = 0
        for j in range(LINE_NUM + 1):
            cnt += line_start_end[i][j]
            mai_cnt[cnt] += 1

    for i in range(1, N + 1):
        print(mai_cnt[i])


main()
