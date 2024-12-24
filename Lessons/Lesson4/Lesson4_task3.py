import random
import copy
numbers = []
for i in range(random.randint(3, 10)):
    numbers.append(i)
print(numbers)
res = []
first_digit = res.append(numbers[0])
second = res.append(numbers[2])
third_digit = res.append(numbers[-2])
print(res)

