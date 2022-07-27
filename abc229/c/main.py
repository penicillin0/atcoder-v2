import sys

input = sys.stdin.readline

n, w = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(key=lambda x: x[0], reverse=True)

ans = 0
x = 0
for a, b in AB:
    able_append_gram = min((w - x), b)
    x += able_append_gram
    ans += able_append_gram * a
print(ans)
