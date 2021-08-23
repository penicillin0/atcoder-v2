import sys
input = sys.stdin.readline

n = int(input())
p, q, r = sorted(map(int, input().split()))


m = 10 ** 4
ans = float('inf')

for a in range(m):
    for b in range(m):
        c = (n - a * p - b * q) // r
        if n == a * p + b * q + c * r:
            ans = min(ans, a + b + c)
print(ans)
