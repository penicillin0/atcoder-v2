import re
import sys


def check_palindrome(s: str) -> bool:
    return s == s[::-1]


input = sys.stdin.readline

S = input().replace('\n', '')

prefix_a_num = 0
suffix_a_num = 0

for i in range(len(S)):
    if S[i] != 'a':
        break
    else:
        prefix_a_num += 1

reversed_S = S[::-1]
for i in range(len(S)):
    if reversed_S[i] != 'a':
        break
    else:
        suffix_a_num += 1

if prefix_a_num == len(S):
    print("Yes")
elif prefix_a_num > suffix_a_num:
    print("No")
elif suffix_a_num >= prefix_a_num:
    is_palindrome = check_palindrome('a' * (suffix_a_num - prefix_a_num) + S)
    print('Yes' if is_palindrome else 'No')
