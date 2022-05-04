import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
odd_A = []
even_A = []

for i in range(2 ** n):
    if i >= 2 ** (n - 1):
        odd_A.append(A[i])
    else:
        even_A.append(A[i])

v = min(max(odd_A), max(even_A))
print(A.index(v) + 1)
