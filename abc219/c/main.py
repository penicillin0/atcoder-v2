import sys
input = sys.stdin.readline

X = input().replace('\n', '')
n = int(input())
S = [input().replace('\n', '') for _ in range(n)]

jisyo_rule = {}
for i, x in enumerate(X):
    jisyo_rule[x] = i + 1

jisyo_rule['*'] = 0


for i in range(n):
    appendix = (10 - len(S[i])) * '*'
    S[i] += appendix


def get_27_value(value: str):
    ret_val = 0
    for i, v in enumerate(value[::-1]):
        ret_val += jisyo_rule[v] * (27 ** i)
    return ret_val


S.sort(key=lambda x: get_27_value(x))
for s in S:
    print(s.replace('*', ''))
