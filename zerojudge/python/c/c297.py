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

print(score)
