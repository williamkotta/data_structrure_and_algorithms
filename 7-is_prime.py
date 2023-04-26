def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    output = is_prime(9)
    print(output)
