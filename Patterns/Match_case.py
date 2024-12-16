number1 = int(input('Enter first number: '))
action = int(input('1. +\n2. -\n3. *\n4. /'))
number2 = int(input('Enter second number: '))

match action:
    case 1:
        print(number1 + number2)
    case 2:
        print(number1 - number2)
    case 3:
        print(number1 * number2)
    case 4:
        if number2 == 0:
            print('Divide for 0 PROHIBIT')
        print(number1 / number2)
    case _:
        print('Invalid value')

# number = (1, 8, 5, 7)
# print(number[-3])
# numbers = [2,6,4,55,7,9,12]
# print(numbers[1:5])
# print(numbers[-1])
# print(numbers[1:5:1])
# print(numbers[::-1])
# print(numbers[3::-1])
# names = ['Petya', 'Vasya']
# name1, name2 = names
# print(name1)
# print(name2)
# print(names)