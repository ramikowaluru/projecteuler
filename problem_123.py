from math import sqrt


def is_prime(n):
    n_sqrt = int(sqrt(n))
    for i in range(2, n_sqrt + 1, 1):
        if n % i == 0:
            print(i)
            return False

    return True


def get_rem(prime, n):
    return ((prime - 1) ** n + (prime + 1) ** n) % prime ** 2


i = 937
j = 7038
while j < 100000000:
    if is_prime(j):
        i += 1
        if get_rem(j, i) > 10000000000:
            print(i, j)
            break
    j += 1