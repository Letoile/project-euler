# -*- coding: utf-8 -*-

"""
Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
------------------------------
Большая сумма

Найдите первые десять цифр суммы следующих ста 50-значных чисел.
"""

def main():
  #5537376230
  with open ("data/problem-13.txt", "r") as myfile:
    data = [long(line.strip()) for line in myfile]
  datasum = str(sum(data))
  print datasum[0:10]


if __name__ == "__main__":
    main()