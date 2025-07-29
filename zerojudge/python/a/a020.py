city = {
    "A": "10", "B": "11", "C": "12", "D": "13", "E": "14",
    "F": "15", "G": "16", "H": "17", "I": "34", "J": "18",
    "K": "19", "L": "20", "M": "21", "N": "22", "O": "35",
    "P": "23", "Q": "24", "R": "25", "S": "26", "T": "27",
    "U": "28", "V": "29", "W": "32", "X": "30", "Y": "31", "Z": "33"
}

line = str(input())
alph = line[0]
rest_num = line[1:]
check = 0

alph_num = city[alph]
check += int(alph_num[0])*1 + int(alph_num[1])*9
for i in range(8):
    check += int(rest_num[i])*(8-i)
check += int(rest_num[-1])

if check % 10 == 0:
    print("real")
else:
    print("fake")
