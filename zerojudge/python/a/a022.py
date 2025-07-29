line = input()
mid = len(line)//2
if len(line) % 2 == 0:
    h1 = line[:mid]
    h2 = line[mid:]
else:
    h1 = line[:mid]
    h2 = line[mid+1:]
h2 = h2[::-1]
ispalindrome = True

for i in range(len(h1)):
    if h1[i] != h2[i]:
        ispalindrome = False
        break
if ispalindrome:
    print("yes")
else:
    print("no")
