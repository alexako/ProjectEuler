#!/bin/python


from math import sqrt


def is_prime(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True


def get_largest_prime_factor(product):
    prime_factors = []
    for i in range(2, int(sqrt(product))):
        if not product % i and is_prime(i):
            prime_factors.append(i)

    return max(prime_factors)

if __name__ == '__main__':
    print get_largest_prime_factor(600851475143)
