numbers = [0, 1, 7, 2, 4, 8]
couples = numbers[::2]
last_digit = numbers[-1]
# print(last_digit)
# print(couples)
for index in couples:
    res = sum(couples)
    print(res * last_digit)
    break