def double_letter(st):
    return st * 2


def main():
    st = "python"
    print("".join(list(map(double_letter, st))))


if __name__ == "__main__":
    main()
