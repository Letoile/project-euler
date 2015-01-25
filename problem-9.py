# -*- coding: utf-8 -*-
"""
Special Pythagorean triplet
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

--------------
Особая тройка Пифагора

Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

"""

def main():
    final_sum = 0
    a, b, c = 0, 0, 0
    for m in range(2, 500):
        for n in range(1, m):
            # EURIKA!
            if 2*m*n + 2*m*m == 1000:
                a, b, c = 2*m*n, m*m - n*n, m*m + n*n
                print(a, b, c)
                print(a*b*c)
                return

if __name__ == "__main__":
   main()