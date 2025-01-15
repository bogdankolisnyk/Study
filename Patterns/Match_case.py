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
import keyword

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
#
# a = int(input("Input a "))
# b = int(input("Input b "))
# i = 0
# while i < a: # Висота
#     j = 0
#     while j < b: # ширина
#         print("*", end='') # рядок не буде переведено
#         j += 1
#     print()
#     i += 1

# my_string = """Python
# 'is'
# awesome
# """
# print(my_string)

# my_string = "Python is awesome"
# print(my_string[6]) # виведе: P
# print(my_string[10]) # виведе: y

# my_string = "python"
# for char in my_string:
#     print(char, end='')
# import keyword
# var = input("Enter variable: ")
# if var in keyword.kwlist:
#     print(type("Wrong variable"))
# else:
#     print(type("Correct variable"))

# n1, n2 = 10, 20
# print(n1 > n2)
# print(type(1 == n2))

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# name = 'mike '
# surname = 'bobik '
# age = 33
# print(name  + surname  + str(age))

# text = "hello my dear friend. how are you."
# search_item = '. '
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentences = search_item.join(result)
#
# print(result_sentences)

# matrix = [
#     [23, 34, 14, 74],
#     [23, 34, 12, 74],
#     [22, 47, 65, 80],
#     [65, 4, 43, 69]
# ]
#
# for row in matrix:
#     for number in row:
#         print(number, end=' ')
#     print()

# import random
#
# matrix = []
#
# for i in range(5):
#     matrix.append([])
#     # print(matrix)
#     for j in range(5):
#         matrix[i].append(random.randint(50, 99))
#         # print(matrix)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# general_diagonal_sum = 0
#
#
#
# for i in range(len(matrix)):
#     general_diagonal_sum += matrix[i][len(matrix[i]) - i - 1]
#     print(matrix[i][len(matrix[i]) - i - 1])
#     i += 1
#
# print(f'General_diagonal_sum: {general_diagonal_sum}')
#
# number = []
#
# for i in range(len(matrix)):
#     number.append(matrix[i][len(matrix[i]) - 1 - i])
# print(number)
# print(f'Min number: {min(number)}')
# print(f'Max number: {max(number)}')

# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()


# text = "Change your mind!"
# var = "a"
# if text.find(var) != -1:
#     print(f'found {var}')
# else:
#     print(f'not found {var}')

# text = ("Change your mind",)
# print(hash(1))
#
# human = {"name": "Alexander",
#         "lastname": "Glock",
#         "age": 36,
#         "address": {"street": "Lisova", "house": 87, "flat": 705}
# }
# #
# # house = human["address"]["house"]
# # print(house) # виведе: 87
# #
# # # # Міняємо значення для квартири
# # human["address"]["flat"] = 700
# # print(human["address"]["flat"])
#
# d2 = human.copy()
# d2['address']["flat"] = '1000'
# print(d2)


# d1 = dict.fromkeys(human)
# print(human.keys())
# print(human.values())
#
# print('Alexander' in human.values())

# from   collections import OrderedDict
# dct = OrderedDict({'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1})
# dct_sec = list(dct.keys())[1]
# dct['orange'] = 1
# dct.move_to_end('banana')
# dct.move_to_end('orange', last=False)
# print(dct.pop(dct_sec))
# print(dct_sec)
# print(dct)  # виведе: OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
# print(dct.popitem(last=False))
# print(len(dct))
# print(dct)

# def say_hello():
#     print(f'Hello {name}')
#     # name = "test"
#     # print(f'Hello {name}')
#     # print(10 * 2)
# say_hello()
# say_hello('Test user')
# name = 'Anton'
# say_hello(name)
# # print(name)
# username = 'Petrov'
# say_hello(username)
import math
# for i in range(10):
#     print(fib(i), end=' ')

square = lambda num1, num2: num1 * num2
print()
print(lambda:print("Hell world!"))
