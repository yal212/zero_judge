while True:
    try:
        s = input()

        def remove_non_alpha(s):
            return ''.join(char for char in s if char.isalpha())
        s = remove_non_alpha(s).lower()
        l = len(s)
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        odd = 0
        for count in chars.values():
            if count % 2 != 0:
                odd += 1
        if l % 2 == 0 and odd == 0:
            print("yes !")
        elif l % 2 == 0:
            print("no...")
        elif l % 2 == 1 and odd == 1:
            print("yes !")
        else:
            print("no...")

    except:
        break
