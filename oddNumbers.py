def print_odd_number(input_list):
    for number in input_list:
        if number % 2 != 0:
            print(number)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers:")
print_odd_number(my_list)