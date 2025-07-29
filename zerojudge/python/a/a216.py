# def f(n):
#     if n == 1:
#         return 1
#     return n + f(n-1)


# def g(n):
#     if n == 1:
#         return 1
#     return f(n) + g(n-1)


# while True:
#     try:
#         n = int(input())
#         print(f(n), g(n))
#     except:
#         break


while True:
    try:
        n = int(input())
    except:
        break
    fn = (n+1)*n//2
    gn = (2+n)*(1+n)*n//6
    print(fn, gn)
