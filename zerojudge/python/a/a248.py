# while True:
#     try:
#         a, b, n = map(int, input().split())
#         ans = a/b
#         print(f"{ans:.{n}f}")
#     except:
#         break


from decimal import Decimal, getcontext, ROUND_DOWN

while True:
    try:
        a, b, n = map(int, input().split())
        getcontext().prec = n + 10  # Ensure enough precision before quantizing
        getcontext().rounding = ROUND_DOWN  # Important: truncate, don't round

        ans = Decimal(a) / Decimal(b)
        # e.g., Decimal('1.0000000000') for n=10
        ans = ans.quantize(Decimal('1.' + '0' * n))
        print(ans)
    except:
        break
