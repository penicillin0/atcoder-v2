import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

if c % 2 == 0:
    print('<' if abs(a) < abs(b) else '>' if abs(a) > abs(b) else '=')
else:
    print('<' if a < b else '>' if a > b else '=')
