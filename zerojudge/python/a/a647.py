# n = int(input())
# for _ in range(n):
#     decide = "keep"
#     buy, sell = map(int, input().split())
#     percent = ((sell-buy)/buy)*100
#     formated_percent = f"{percent:.2f}"
#     if percent <= -7.00 or percent >= 10.00:
#         decide = "dispose"
#     print(f"{formated_percent}% {decide}")


# from decimal import Decimal, ROUND_HALF_UP

# n = int(input())
# for _ in range(n):
#     buy, sell = map(int, input().split())
#     percent = Decimal((sell - buy) * 100) / Decimal(buy)
#     percent = percent.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
#     decide = "keep"
#     if percent < Decimal("-7.00") or percent > Decimal("10.00"):
#         decide = "dispose"
#     print(f"{percent}% {decide}")


n = int(input())
for i in range(n):
    m, p = map(int, input().split())
    r = (p-m)/m*100
    if r < 0:
        r = r - 0.000001
    elif r > 0:
        r = r + 0.000001
    if r >= 10 or r <= -7:
        t = 'dispose'
    else:
        t = 'keep'
    print(f'{r:.2f}% {t}')
