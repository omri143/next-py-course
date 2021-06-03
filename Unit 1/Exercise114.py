import functools


def sum_of_digits(number):
    return functools.reduce(sum_digits, export_digits_to_list(number))


def export_digits_to_list(number):
    lst = []
    while number > 0:
        dig = number % 10
        number = int(number / 10)
        lst.append(dig)
    return lst


def sum_digits(a, b):
    return a + b


print(sum_of_digits(9))
