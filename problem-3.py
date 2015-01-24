# -*- coding: utf-8 -*-
"""
Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

-----------------------
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

import math

# without optimization

def eratosphen(num):
    sieve = [0 for x in range(num+1)]
    sieve[1] = 0
    for i in range(2, num):
        sieve[i] = 1
    j = 2
    while j*j <= num:
        if sieve[j] == 1:
            for l in range(j*j, num, j):
                sieve[l] = 0
        j += 1
    return sieve


def main():
    number = 600851475143
    possible_dividers = eratosphen(int(math.sqrt(number)) + 1)
    dividers = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if possible_dividers[i] == 1:
            if not number % i:
                dividers.append(i)
    print(dividers[-1])

if __name__ == "__main__":
    main()