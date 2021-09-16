import sys
import math
input = sys.stdin.readline


a, b, c = map(int, input().split())

leng = math.gcd(math.gcd(a, b), c)
print(a // leng + b // leng + c // leng - 3)
