numbers = []
first_part_of_list = round(len(numbers) / 2)
second_part_of_list = len(numbers) // 2
if first_part_of_list == 0:
    print(numbers, '=>', '[',numbers[0:first_part_of_list+1],',',numbers[second_part_of_list+1:len(numbers)],']')
elif first_part_of_list > second_part_of_list or first_part_of_list == 0:
    print(numbers, '=>', '[',numbers[0:first_part_of_list],',',numbers[second_part_of_list+1:len(numbers)],']')
elif first_part_of_list == second_part_of_list:
    print(numbers, '=>', '[',numbers[0:first_part_of_list],',',numbers[second_part_of_list:len(numbers)],']')
else:
    print(numbers[first_part_of_list], numbers[second_part_of_list])
