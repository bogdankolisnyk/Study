numbers = [0, 1, 0, 12, 3]
digits = numbers.copy()
digit_zero = numbers.copy()

for number in digits:
    if number != 0:
        print(number, end=' ')
for zero in digit_zero:
    if zero == 0:
        print(zero, end=' ')

