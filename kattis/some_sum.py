n = int(input())
hn = n//2
if n % 2 == 0:
    if hn % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Either")
