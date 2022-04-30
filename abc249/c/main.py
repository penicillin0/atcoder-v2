import sys

input = sys.stdin.readline

n, k = map(int, input().split())
S = [input().replace('\n', '') for _ in range(n)]

ans = 0
for i in range(2 ** n):
    str_i = bin(i)[2:].zfill(n)
    selected = []
    for j, bit in enumerate(str_i):
        if bit == '0':
            continue
        else:
            selected.append(S[j])
    letter_count_dict = {}
    for s in selected:
        for c in s:
            if c not in letter_count_dict:
                letter_count_dict[c] = 1
            else:
                letter_count_dict[c] += 1

    tmp = 0
    for key, value in letter_count_dict.items():
        if value == k:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
