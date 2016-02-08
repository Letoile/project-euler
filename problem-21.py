# -*- coding: utf-8 -*-

"""
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

---------------------
Дружественные числа

Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным
числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 -
1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.

"""

def main():
    BIG_NUMBER = 10000
    divisors_sum = [0, 1]
    browsed = []
    amicables = []
    amicables_sum = 0
    for x in xrange(2, BIG_NUMBER):
        temp = 0
        for y in range(1, int(x/2) + 1):
            if x % y == 0:
                temp += y
        divisors_sum.append(temp)
    for x in xrange(1, BIG_NUMBER):
        if x not in browsed:
            sum = divisors_sum[x]
            if sum <= len(divisors_sum) and divisors_sum[sum] == x and sum != x:
                amicables_sum += sum + x
                amicables.extend([sum, x])
                browsed.extend([sum, x])
    print amicables_sum
    print amicables



if __name__ == "__main__":
    main()