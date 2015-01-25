# -*- coding: utf-8 -*-
"""
Summation of primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

----------------------
Сложение простых чисел

Сумма простых чисел меньше 10 - это 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""


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
    max_number = 2000000
    primes_array = eratosphen(max_number - 1)
    sum_ = sum(idx for idx in range(0, max_number) if primes_array[idx] == 1)
    print(sum_)


if __name__ == "__main__":
   main()