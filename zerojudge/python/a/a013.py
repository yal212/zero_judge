roman_nums = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
              "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

dif = 0


def int_to_roman(n):
    roman = ""
    for char, num in roman_nums.items():
        while n >= num:
            roman += char
            n -= num
    return roman


def roman_to_int(n):
    ans = 0
    temp = 0
    for char in n:
        if roman_nums[char] > temp:
            ans = ans - temp * 2 + roman_nums[char]
        else:
            ans += roman_nums[char]
        temp = roman_nums[char]
    return ans


while True:

    nums = input().split()

    if len(nums) == 2:
        num_1, num_2 = map(str, nums)
    else:
        break

    dif = abs(roman_to_int(num_1) - roman_to_int(num_2))
    if dif == 0:
        print("ZERO")
    else:
        print(int_to_roman(dif))
