import sys
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())


# ans0
ab_num = 2 * y
if x > y:
    ans0 = ab_num * c + (x - y) * a
else:
    ans0 = ab_num * c

# ans1
ab_num = 2 * x
if y > x:
    ans1 = ab_num * c + (y - x) * b
else:
    ans1 = ab_num * c

# ans2
ans3 = a * x + b * y

print(min(min(ans0, ans1), ans3))
