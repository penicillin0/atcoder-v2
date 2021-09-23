from collections import Counter

N = int(input())
A = list(map(int, input().split()))
count_a = Counter(A)

ans = 0
for a in A:
    product_cnt = N - count_a[a]
    ans += product_cnt

print(ans // 2)
