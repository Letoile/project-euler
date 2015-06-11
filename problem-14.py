# -*- coding: utf-8 -*-

"""
Longest Collatz sequence


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

---------------------
Самая длинная последовательность Коллатца

Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - чётное)
n → 3n + 1 (n - нечётное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: После начала последовательности элементы могут быть больше миллиона.

"""
import time

# approx. 3.86190104485 seconds YAHOO!
def main():
    start = time.time()
    known_sums = {key: 0 for key in range(1,1000000)}
    longest = 0
    final_num = 0

    for number in range(1, 1000000):
        temp = number
        count = 1

        while temp > 1:
            if temp % 2 == 0:
                temp = temp / 2
            else:
                temp = 3 * temp + 1  
            if temp in known_sums and known_sums[temp] != 0:
                count += known_sums[temp]
                break
            count += 1    

        known_sums[number] = count      
        if count > longest:
            longest = count
            final_num = number

    elapsed = (time.time() - start)    
    print final_num
    print "%s seconds" % (elapsed)  

if __name__ == "__main__":
    main()