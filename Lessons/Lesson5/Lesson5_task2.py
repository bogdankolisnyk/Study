while True:
    number1 = int(input('Enter first digit: '))

    action = input('Enter action (+, -, *, /): ')

    number2 = int(input('Enter second digit: '))

    if action == '+':
        print(f"Result: {number1} + {number2} = {number1 + number2}")
    elif action == '-':
        print(f"Result: {number1} - {number2} = {number1 - number2}")
    elif action == '*':
        print(f"Result: {number1} * {number2} = {number1 * number2}")
    elif action == '/' and number2 == 0:
        print('Error, division by zero is prohibited!')
    elif action == '/':
        print(f"Result: {number1} / {number2} = {number1 / number2}")
    else:
        print('Invalid operation.')

    continue_calculation = input("Do you want to continue? (y/n): ").strip().lower()
    if continue_calculation != 'y':
        print("Goodbye!")
        break