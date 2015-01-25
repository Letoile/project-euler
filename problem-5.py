# -*- coding: utf-8 -*-
"""
Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

----------------------------------
Наименьшее кратное

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

#every number is divided by 1,
#4, 6, 8, .... is divided by 2
#6, 9, 12, .. is divided by 3
# so we can remove such numbers from sequence
#sequence = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

from functools import reduce


def euclid(a, b):
    """
    # Euclid algorithm for seeking GCD
    """
    return a if b == 0 else euclid(b, a % b)


def lcm(numbers):
    """
    Functional implementation of least common multiple algorithm
    """
    return reduce(lambda x, y: (x*y)/euclid(x, y), numbers, 1)


def main():
    sequence = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(lcm(sequence))

if __name__ == "__main__":
    main()