import sys
input = sys.stdin.readline

n = int(input())

ans = set()

if n % 2 == 1:
    print()


for bin_i in range(2 ** n):
    str_i = bin(bin_i)[2:].replace('1', '(').replace('0', ')').zfill(n)
    cnt = 0
    for ch in str_i:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        ans.add(str_i)


for a in sorted(ans):
    print(a)
