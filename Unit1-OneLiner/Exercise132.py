def is_prime(number):
    return number > 1 and [True for i in range(2, int(number ** 0.5) + 1) if number % i == 0] == []


print(is_prime(43))
