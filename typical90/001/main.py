N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

part_A = [A[0]]
for i in range(1, N):
    part_A.append(A[i] - A[i - 1])
part_A.append(L - A[-1])


# x以上でk回以上切れるか
def can_divide(x):
    cnt = 0
    part = 0
    for a in part_A:
        part += a
        if part >= x:
            cnt += 1
            part = 0
    return cnt >= K + 1


left, mid, right = 0, L // 2, L

while not (left == mid or mid == right):
    if can_divide(mid):
        left = mid
        mid = (mid + right) // 2
    else:
        right = mid
        mid = (mid + left) // 2
print(mid)
