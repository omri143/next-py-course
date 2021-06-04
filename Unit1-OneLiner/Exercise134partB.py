PASSWORD = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


def decode(string):
    return ''.join(list(map(lambda char: chr(ord(char) + 2) if char.isalpha() else char, string)))


def main():
    print(decode(PASSWORD))


if __name__ == "__main__":
    main()
