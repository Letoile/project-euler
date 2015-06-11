# -*- coding: utf-8 -*-

"""
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

---------------------
Сумма цифр степени

2^15 = 32768, сумма цифр 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
"""
import time
import math

#1366
def main():
    start = time.time()
    multiple = long(math.pow(2,1000))
    sum_ = sum([int(i) for i in str(multiple)])
    elapsed = (time.time() - start)    
    print sum_
    print "%s seconds" % (elapsed)  

if __name__ == "__main__":
    main()