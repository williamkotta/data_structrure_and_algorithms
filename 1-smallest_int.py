def get_smallest_integer(my_list):
    number = my_list[0]
    for value in my_list:
        if number > value:
            number = value
    return number


if __name__ == "__main__":
    output = get_smallest_integer([10, 55, 46, 78, 127])
    print(output)
