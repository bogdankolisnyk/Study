number1 = int(input('Enter first digit: '))
action = input('Enter action: ')
number2 = int(input('Enter second digit: '))
if action == '+':
    print(number1 + number2)
elif action == '-':
    print(number1 - number2)
elif action == '*':
    print(number1 * number2)
elif action == '/' and number2 == 0:
    print('Error, div for ZERO prohibit!')
elif action == '/':
    print(number1 / number2)
else:
    print('Invalid value')
