import sys

input = sys.stdin.readline


n = int(input())
ans = ['0', '1']
for i in range(2, n + 1):
    ans.append(ans[i - 1] + ' ' + str(i) + ' ' + ans[i - 1])

print(ans[-1])
