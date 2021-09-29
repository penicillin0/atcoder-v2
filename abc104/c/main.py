import sys
input = sys.stdin.readline

D, G = map(int, input().split())
PC = [list(map(int, input().split())) for _ in range(D)]


ans = 10 ** 9
for i in range(2 ** D):
    problem_cnt = 0
    all_point = 0
    comp_set = set()
    str_i = bin(i)[2:].zfill(D)

    # 0: ボーナスなし, 1: ボーナスあり
    for problem_num, comp in enumerate(str_i):
        if comp == '1':
            cnt, comp_point = PC[problem_num]
            point = (problem_num + 1) * 100
            problem_cnt += cnt
            all_point += (point * cnt)
            all_point += comp_point
            comp_set.add(problem_num)

    # この時点でG点を超えて入れえば終了
    if G <= all_point:
        ans = min(ans, problem_cnt)
        continue

    # 超えていない場合は1種類でG点を超えられるか調べる
    # 余っている問題の特定
    should_solve_problem_num = -1
    for problem_num in range(D - 1, -1, -1):
        if problem_num in comp_set:
            continue
        else:
            should_solve_problem_num = problem_num
            break

    solve_num = (G - all_point) // ((should_solve_problem_num + 1) * 100)
    if (G - all_point) > solve_num * ((should_solve_problem_num + 1) * 100):
        solve_num += 1

    if solve_num < PC[should_solve_problem_num][0]:
        all_point += solve_num * (should_solve_problem_num + 1) * 100
        problem_cnt += solve_num
    else:
        continue

    if all_point >= G:
        ans = min(ans, problem_cnt)

print(ans)
