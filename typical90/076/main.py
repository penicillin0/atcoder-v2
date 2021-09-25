import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = sum(A)

double_A = A + A

l, r = 0, 1
cake_area = double_A[l]

while r < 2 * N - 1:
    # print("l, r, cake_area", l, r, cake_area)
    if S == cake_area * 10:
        print("Yes")
        exit()

    if cake_area * 10 > S:
        cake_area -= double_A[l]
        l += 1
    else:
        cake_area += double_A[r]
        r += 1


print("No")
