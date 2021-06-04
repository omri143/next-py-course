PASSWORD = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


def shift_char(char, key):
    return chr(ord(char) + (key % 26))  # 26 letter on the american alphabet


def main():
    password_decrypted = []
    for char in PASSWORD:
        if char.isalpha():
            password_decrypted.append(shift_char(char, 2))
        else:
            password_decrypted.append(char)
    print("".join(password_decrypted))


if __name__ == "__main__":
    main()
