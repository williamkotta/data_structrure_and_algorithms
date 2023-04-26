def two_indices(nums, target):
    for i, first_no in enumerate(nums):
        for j, second_no in enumerate(nums):
            sum = first_no + second_no
            if sum == target:
                return [i, j]


if __name__ == "__main__":
    output = two_indices([2, 7, 11, 15], 9)
    print(output)
