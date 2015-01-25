# -*- coding: utf-8 -*-
"""
10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

-----------------
10001-ое простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""

#without optimization, too slow
#todo make it faster

import math
from datetime import datetime

def is_prime_number(num):
    if num == 1:
        return False
    for divider in range(2, int(math.sqrt(num)) + 1):
        if num % divider == 0:
            return False
    return True


def main():
    seeking_idx = 10001
    primes = []
    counter = 2
    start = datetime.now()
    while len(primes) < seeking_idx:
        if is_prime_number(counter):
            primes.append(counter)
        counter += 1
    end = datetime.now() - start
    print(primes[-1])
    print("time: ", str(end))

if __name__ == "__main__":
    main()