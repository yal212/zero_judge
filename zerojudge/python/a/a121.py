# def prime(a, b):
#     ans = 0
#     for num in range(a, b+1):
#         if num < 2:
#             continue
#         for n in range(2, int(num**0.5)+1):
#             if num % n == 0:
#                 break
#         else:
#             ans += 1
#     return ans


# while True:
#     try:
#         a, b = map(int, input().split())
#         print(prime(a, b))
#     except:
#         break

def prime(a, b):
    ans = 0
    for num in range(a, b+1):
        if num < 2:
            continue
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                break
        else:
            ans += 1
    return ans


while True:
    try:
        a, b = map(int, input().split())
        print(prime(a, b))
    except:
        break
