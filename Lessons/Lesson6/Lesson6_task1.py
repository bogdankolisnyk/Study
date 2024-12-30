import string

input_str = input("Enter two letters separated by a dash (e.g., a-z): ")

letter1, letter2 = input_str.split('-')
all_letters = string.ascii_letters

start_index = all_letters.index(letter1)
end_index = all_letters.index(letter2)

result = all_letters[start_index:end_index + 1]
print(result)