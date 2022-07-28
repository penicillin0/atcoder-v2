import sys

input = sys.stdin.readline

n = int(input())

S = [input().rstrip() for _ in range(n)]

record = {}

for s in S:
    if s in record:
        print(s + "(" + str(record[s]) + ")")
        record[s] += 1
    else:
        print(s)
        record[s] = 1
