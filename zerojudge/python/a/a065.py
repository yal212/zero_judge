word = input()
passwd = ""
for i, char in enumerate(word):
    if i+1 == len(word):
        continue
    else:
        passwd += str(abs(ord(char)-ord(word[i+1])))
print(passwd)
