numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
digits = []
digit_zero = []

for i in numbers:
    if i != 0:
        digits.append(i)
    else:
        digit_zero.append(i)
print(digits + digit_zero)

