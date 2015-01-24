# -*- coding: utf-8 -*-

"""
Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

----------------------------
Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трёхзначных чисел.
"""

# without optimization

def digits_num(number):
    count = 0
    while number != 0:
        number /= 10
        count += 1
    return count


def is_palindrom(number):
    nnumber = number
    digits = digits_num(nnumber)
    right_part = 0
    for num in range(1, (digits / 2) + 1):
        right_part *= 10
        right_part += nnumber % 10
        nnumber /= 10
    if (digits % 2) != 0:
        nnumber /= 10
    left_part = str(nnumber)
    right_part = str(right_part)
    return left_part == right_part


def main():
    multis = []
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            multi = i * j
            if is_palindrom(multi):
                multis.append(multi)
    return max(multis)

if __name__ == "__main__":
    print(main())