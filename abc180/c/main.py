import sys

input = sys.stdin.readline


def get_all_multiple(n):
    multi = set()
    for i in range(1, int(pow(n, 1/2)) + 1):
        if n % i == 0:
            multi.add(i)
            multi.add(n // i)
    return multi


n = int(input())
multi_list = list(get_all_multiple(n))
multi_list.sort()
for a in multi_list:
    print(a)
