a, b = map(int, input().split())
gcd = 1

while b:
    a, b = b, a % b
gcd = a
print(a)

# below are TLE

# big = max(n1, n2)
# small = min(n1, n2)

# if big % small == 0:
#     gcd = small
# else:
#     for i in range(2, small//2+2):
#         if n1 % i == 0 and n2 % i == 0:
#             gcd = i
# print(gcd)


# def FindFactors(n):
#     factors = set()

#     for i in range(1, n//2+1):
#         if n % i == 0:
#             factors.add(i)
#             factors.add(n//i)

#     return factors

# n1_facs = FindFactors(n1)
# n2_facs = FindFactors(n2)

# for n1_fac in n1_facs:
#     if n1_fac in n2_facs:
#         gcd = max(gcd, n1_fac)

# print(gcd)
