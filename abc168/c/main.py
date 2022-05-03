import math
import sys

input = sys.stdin.readline

a, b, hour, minute = map(int, input().split())

pace = hour + minute / 60
sita = 360 * pace / 12 - 360 * minute / 60
sita = min(sita, 360 - sita)
c_2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(sita))
c = math.sqrt(c_2)
print(c)
# print(pace, sita)
