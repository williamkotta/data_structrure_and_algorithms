def find_first_occurrence(my_list, num):
    for index, item in enumerate(my_list):
        if num == item:
            return index


if __name__ == "__main__":
    output = find_first_occurrence([10, 11, 15, 67], 11)
    print(output)
