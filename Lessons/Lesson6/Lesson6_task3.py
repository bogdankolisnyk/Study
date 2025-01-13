number = int(input("Enter a number: "))

while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product
    print(number)

print(f"Result: {number}")