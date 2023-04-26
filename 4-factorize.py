def factorize(number):
    factors = []
    factor = 2
    while(number > 1):
        if(number % factor == 0):
            factors.append(factor)
            number = number / factor
        else:
            factor = factor + 1
    return factors


if __name__ == "__main__":
    output = factorize(630)
    print(output)
