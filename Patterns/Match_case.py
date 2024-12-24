# number1 = int(input('Enter first number: '))
# action = int(input('1. +\n2. -\n3. *\n4. /'))
# number2 = int(input('Enter second number: '))
#
# match action:
#     case 1:
#         print(number1 + number2)
#     case 2:
#         print(number1 - number2)
#     case 3:
#         print(number1 * number2)
#     case 4:
#         if number2 == 0:
#             print('Divide for 0 PROHIBIT')
#         print(number1 / number2)
#     case _:
#         print('Invalid value')
# from ctypes import HRESULT
# from operator import truediv

# number = (1, 8, 5, 7)
# print(number[-3])
# numbers = [2,6,4,55,7,9,12]
# # numbers[3] = 1
# numbers.append(2)
# numbers.insert(1, 3)
# numbers.remove(55)
# del numbers[0]
# print(numbers)
# print(numbers[::-1])
# print(numbers[-1])
# print(numbers[1:5:1])
# print(numbers[::-1])
# print(numbers[3::-1])

# names = ['Petya', 'Vasya']
# name1, name2 = names
# print(name1)
# print(name2)
# print(names)

numbers = [1, 3, 2, 5, 77, 1, 6, 1]
numbers_1 = [77, 5, 7, 4]
# numbers.remove(1)
# print(numbers)
# print(numbers.index(1))
# print(numbers.pop(3))
# print(numbers)
# print(numbers.count(1))
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# if not 77 in numbers:
#     print('no')
# else:
#     print('yes')
# print(len(numbers))
# numbers *= numbers_1
# print(numbers)

# price = 10
# my_money = 15
# my_money -= price
# print(my_money)

# orange_price = .5
# my_money = 20
# tea_price = 14
# if my_money > orange_price:
#     print("I buy orange")
# else:
# # Вкладений умовний оператор if зі своїм блоком else
#     if my_money > tea_price:
#         print("Not orange, just tea")
#     else:
#         print("I buy apple")
# print("The end")

# number_a = 17
# number_b = 21
#
# if number_b > 20 or number_a > 20:
#     if number_a > 20:
#         print('>20')
#     print("Yes")
# else:
#     print("No")

# number_a = 17
# if not number_a > 20:
#     print("Yes")
# else:
#     print("No")

# text = "hello. goodbye."
# separator = '. '
# sentences = text.split(separator)
# print(sentences)
#
# result = []
#
# for sent in sentences:
#     result.append(sent.capitalize())
# print(result)
# result_sentence = separator.join(result)
# print(result_sentence)

# num = 0
#
# while True:
#
#     if num == 3:
#         num += 1
#         print('You win!')
#         continue
#     if num > 5:
#         print('You lose')
#         break
#     print(num)
#     num += 1

# while True:
#     rating = int(input('Enter your rating from 1 to 3: (0 for exit)'))
#
#     if rating == 0:
#         print('Exit')
#         break
#     if rating > 1 or rating > 3:
#         print('Invalid value!')
#         continue
#     match rating:
#         case 1:
#             print('Bad rating')
#         case 2:
#             print('Normal rating')
#         case 3:
#             print('Good rating')

# number = 0
#
# while number < 10:
#     number = number + 1 # До continue !!!!
#     if number == 5:
#         continue
#     print(number)

# number = int(input("input positive number "))
# i = 2
# while i < number:
#     if number % i == 0:
# 				# Якщо число ділиться без залишку на інше число, то це число не є простим
#         print("It is not a prime number")
#         break
#     i = i + 1
# else: # виконається тільки якщо break в циклі не буде викликаний.
#     print("It is a prime number")

a = int(input("Input a "))
b = int(input("Input b "))
i = 0
while i < a: # Висота
    j = 0
    while j < b: # ширина
        print("*", end='') # рядок не буде переведено
        j += 1
    print()
    i += 1
