at_bats = [list(map(str, input().split())) for _ in range(9)]
b = int(input())
outs = 0
total_outs = 0
bases = []
batter = 0
rounds = 1
score = 0
hit = ["1B", "2B", "3B", "HR"]


def check(bases):
    if not bases:
        return 0
    if bases[0] >= 4:
        bases.pop(0)
        return check(bases) + 1
    else:
        return 0


while total_outs < b:
    # print(
    #     f"before: batter {batter}, rounds {rounds}, outcome {None}, bases {bases}, score {score}, outs {outs}")
    outcome = at_bats[batter][rounds]
    if outcome in hit:
        bases = [base + hit.index(outcome) + 1 for base in bases]
        bases.append(hit.index(outcome)+1)
        score += check(bases)
    else:
        total_outs += 1
        outs += 1
    batter += 1
    if outs != 0 and outs == 3:
        bases = []
        outs = 0
    if batter == 9:
        batter = 0
        rounds += 1
    # print(
    #     f"after: batter {batter}, rounds {rounds}, outcome {outcome}, bases {bases}, score {score}, outs {outs}")


print(score)


# 範例輸入 #1
# 5 1B 1B FO GO 1B
# 5 1B 2B FO FO SO
# 4 SO HR SO 1B
# 4 FO FO FO HR
# 4 1B 1B 1B 1B
# 4 GO GO 3B GO
# 4 1B GO GO SO
# 4 SO GO 2B 2B
# 4 3B GO GO FO
# 3
# 範例輸出 #1
# 0
# 範例輸入 #2
# 5 1B 1B FO GO 1B
# 5 1B 2B FO FO SO
# 4 SO HR SO 1B
# 4 FO FO FO HR
# 4 1B 1B 1B 1B
# 4 GO GO 3B GO
# 4 1B GO GO SO
# 4 SO GO 2B 2B
# 4 3B GO GO FO
# 6
# 範例輸出 #2
# 5
