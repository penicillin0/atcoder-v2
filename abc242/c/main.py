import sys

input = sys.stdin.readline

NUM = 998244353

n = int(input())

keta = [[1] * 9 for _ in range(n)]
# print(keta)

for i in range(n - 1):
    for j in range(9):
        keta[i + 1][j] = keta[i][j]
    for j in range(9):
        a = keta[i][j]

        if j == 0:
            keta[i + 1][j + 1] += a
            keta[i + 1][j + 1] %= NUM
        elif j == 8:
            keta[i + 1][j - 1] += a
            keta[i + 1][j - 1] %= NUM
        else:
            keta[i + 1][j + 1] += a
            keta[i + 1][j - 1] += a
            keta[i + 1][j + 1] %= NUM
            keta[i + 1][j - 1] %= NUM
# print(keta)
print(sum(keta[-1]) % NUM)
