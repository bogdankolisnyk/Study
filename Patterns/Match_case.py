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
