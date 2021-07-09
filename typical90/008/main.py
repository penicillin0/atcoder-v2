N = int(input())
S = input()

cnt = 0
r_cnt = {-1: 0}
for idx, s in enumerate(S[::-1]):
    if s == 'r':
        cnt += 1
        r_cnt[idx] = cnt
    else:
        r_cnt[idx] = r_cnt[idx-1]

cnt_dict = {}
for key in 'atcode':
    cnt_dict[key] = {i: 0 for i in range(-1, N)}
cnt_dict['r'] = r_cnt

for i in range(6):
    previous, make = 'redocta'[i], 'redocta'[i + 1]
    previous_dict = cnt_dict[previous]
    make_dict = cnt_dict[make]
    for idx, s in enumerate(S[::-1]):
        if s == make:
            make_dict[idx] = previous_dict[idx - 1] + make_dict[idx - 1]
        else:
            make_dict[idx] = make_dict[idx - 1]

print(cnt_dict['a'][N - 1] % (10 ** 9 + 7))
