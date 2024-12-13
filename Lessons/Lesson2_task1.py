number = int(input("Enter number of 4 digits: "))
number1 = number // 1000
number2 = number // 100 % 10
number3 = number // 10 % 10
number4 = number % 10
print(number1, number2, number3, number4, sep ='\n')