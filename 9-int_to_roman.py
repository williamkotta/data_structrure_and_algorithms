def int_to_roman(n):
    number = [1, 4, 5, 9, 10, 40, 50, 90,
              100, 400, 500, 900, 1000]
    symbol = ["I", "IV", "V", "IX", "X", "XL",
              "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    string = ""
    while n:
        quotient = n // number[i]
        n = n % number[i]
        while quotient:
            string = string + symbol[i]
            quotient = quotient - 1
        i = i - 1
    return string


if __name__ == "__main__":
    output = int_to_roman(1904)
    print(output)
