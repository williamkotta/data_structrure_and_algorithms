def sum_even_numbers(my_list):
    total = 0
    for index, number in enumerate(my_list):
        if(number % 2 == 0):
            total = total + my_list[index]
    return total


if __name__ == "__main__":
    output = sum_even_numbers([33, 34, 53, 54, 73, 74])
    print(output)
