number = int(input("Enter number of 5 digits: "))
number1 =number // 10000
number2 = number // 1000 % 10
number3 = number // 100 % 10
number4 = number // 10 % 10
number5 = number % 10
print(number5 * 10000 + number4 * 1000 + number3 * 100 + number2 * 10 + number1)