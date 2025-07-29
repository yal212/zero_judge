def next_element(a):
    # Write code here
    d = a[1] - a[0]

    return a[-1] + d


s = input()
a = list(map(int, s.strip("[]").split(",")))

print(next_element(a))
