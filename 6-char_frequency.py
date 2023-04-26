def character_frequency(string):
    dictionary = dict()
    for i in string.lower():
        if i.isalnum() is True and i.isdigit() is False:
            frequency = 0
            for j in string.lower():
                if i == j:
                    frequency = frequency + 1
            dictionary[i] = frequency
    return dictionary


if __name__ == "__main__":
    output = character_frequency("1. GROUP NUMBER 4 CSN")
    print(output)
