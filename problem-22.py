# -*- coding: utf-8 -*-

"""
Names scores

Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names, begin
by sorting it into alphabetical order. Then working out the alphabetical value
 for each name, multiply this value by its alphabetical position
 in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

---------------------
Очки за имена

Используйте names.txt (правый клик и 'Save Link/Target As...'),
текстовый файл размером 46 КБ, содержащий более пяти тысяч имён.
Начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение
на порядковый номер имени в отсортированном списке для получения
количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN
(алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является
938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имён в файле?
"""

import string


def main():
    alphabet = list(string.ascii_uppercase)
    scores = 0
    with open ("data/names.txt", "r") as myfile:
      for line in myfile:
          line = line.replace('"', '')
          names = line.split(",")
    names.sort()
    for idx, name in enumerate(names):
        score = sum(alphabet.index(letter) + 1 for letter in list(name))
        scores += score * (idx+1)
    print scores


if __name__ == "__main__":
    main()
