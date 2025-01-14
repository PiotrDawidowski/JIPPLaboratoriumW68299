def analizuj(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    tuples = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numbers, default=None)
    longest_string = max(strings, key=len, default=None)
    largest_tuple = max(tuples, key=len, default=None)

    return {
        "maksymalna liczba": max_number,
        "najdłuższy ciąg": longest_string,
        "Największa krotka": largest_tuple
    }

data = [123, "najdłuższy_string", (6, 2, 5), (9, 12), "krótki_string", 3.14]
result = analizuj(data)
print(result)