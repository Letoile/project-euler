# -*- coding: utf-8 -*-
"""
Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

----------------
Разность между суммой квадратов и квадратом суммы

Сумма квадратов первых десяти натуральных чисел
1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел
(1 + 2 + ... + 10)^2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
"""


# difference can be find by summing double multiples of every pair of number sequence,
# because square of sum = sum of square + double multiples of every pair.
# e.g. for [1, 2, 3] diff = 2*1*2 + 2*1*3 + 2*2*3
# but this solution is slow

import math
from datetime import datetime


def sum_of_squares(numbers):
    return sum([x*x for x in numbers])


def square_of_sum(numbers):
    return math.pow(sum([x for x in numbers]), 2)


def main():
    #regular implementation
    start = datetime.now()
    numbers = [x for x in range(1, 101)]
    sum = sum_of_squares(numbers)
    square = square_of_sum(numbers)
    result_1 = square - sum
    time_1 = datetime.now() - start

    # cool polynomial implementation (fast and simple)
    n = 100
    start = datetime.now()
    result_2 = (n**4)/4.0 + (n**3)/6.0 - (n**2)/4.0 - n/6.0
    time_2 = datetime.now() - start

    print(result_1 == result_2)
    print("first time: ", str(time_1), "; second time: ", str(time_2))

if __name__ == "__main__":
    main()