# -*- coding: utf-8 -*-

"""
Factorial digit sum



n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
---------------------
Сумма цифр факториала

n! означает n × (n − 1) × ... × 3 × 2 × 1

Найдите сумму цифр в числе 100!.
"""

import time

def prod_tree(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right
    mediana = (right + left) // 2
    return prod_tree(left, mediana) * prod_tree(mediana + 1, right)


def fact_tree(number):
    if number < 0:
        return 0
    if number == 0:
        return 1
    if number == 1 or number == 2:
        return number
    return prod_tree(2,number)

def sum_fact_num(number):
    result = 0
    for letter in str(number):
        result += int(letter)
    return result

def main():
    start = time.time()
    result = fact_tree(100)
    result_sum = sum_fact_num(result)
    elapsed = time.time() - start
    print result_sum
    print "%s seconds" % (elapsed)

if __name__ == "__main__":
    main()
