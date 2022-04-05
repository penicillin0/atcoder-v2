import sys

input = sys.stdin.readline

n, k, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)


for i in range(len(A)):
    if k == 0:
        break
    mai = min(A[i] // x, k)
    k -= mai
    A[i] -= mai * x


if k != 0:
    A.sort(reverse=True)
    for i in range(len(A)):
        if k == 0:
            break
        mai = 1
        k -= mai
        A[i] = 0

print(sum(A))
