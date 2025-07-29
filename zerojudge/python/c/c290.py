num = input()
odd = [int(num[i]) for i in range(len(num)) if i % 2 != 0]
even = [int(num[i]) for i in range(len(num)) if i % 2 == 0]

odd_s = sum(odd)
even_s = sum(even)

print(abs(odd_s-even_s))
