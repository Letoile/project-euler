# -*- coding: utf-8 -*-

"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

---------------------
Счет букв в числительных

Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?

Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
"""

import time

ONES = ["","one","two","three","four","five","six","seven","eight","nine","ten",
      "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

TENS = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

HUNDREDS = ["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred",
      "sevenhundred","eighthundred","ninehundred"]


def get_word(number):
	if number < 20:
		return ONES[number]

	if number == 1000:
		return "onethousand"

	if number < 100:
		return TENS[number // 10] + get_word(number % 10)	

	hundred_numb = get_word(number % 100)
	
	if len(hundred_numb) > 0:
		hundred_numb = hundred_numb + "and"

	result = HUNDREDS[number // 100] + hundred_numb	  
	return result        


def main():
    start = time.time()
    result = 0

    for num in range(1, 1001):
    	_len = len(get_word(num))
    	#print "Number = %d, length = %s" % (num, _len)
    	result += _len

    elapsed = (time.time() - start)    
    print result
    print "%s seconds" % (elapsed)  

if __name__ == "__main__":
    main()