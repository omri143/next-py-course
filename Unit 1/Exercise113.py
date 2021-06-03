def four_dividers(number):
    return list(filter(condition, range(1, number)))


def condition(number):
    return number % 4 == 0


def main():
    print(four_dividers(9))


if __name__ == "__main__":
    main()
