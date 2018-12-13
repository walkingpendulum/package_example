from itertools import zip_longest


def cleaned_seq(sequence):
    yield from map(str.lower, filter(str.isalpha, sequence))


def is_palindrome(sequence):
    if not sequence:
        return True

    return all(x == y for x, y in zip_longest(cleaned_seq(sequence), reversed(list(cleaned_seq(sequence)))))
